import pandas as pd
import torch
from data.prompts import BENCHMARK_DATASETS
from models.model_harness import ModelHarness
from evaluation.activation_similarity import compute_tensor_cosine_similarity

def run_activation_pipeline(model_names: list, prompt_template_fn) -> pd.DataFrame:
    records = []
    
    for m_name in model_names:
        try:
            harness = ModelHarness(m_name)
        except Exception as e:
            print(f"Skipping activation tracking for {m_name}: {e}")
            continue
            
        for prob in BENCHMARK_DATASETS:
            clean_prompt = prompt_template_fn(prob["clean"])
            misleading_prompt = prompt_template_fn(prob["misleading"])
            
            clean_states = harness.get_layer_representations(clean_prompt)
            misleading_states = harness.get_layer_representations(misleading_prompt)
            
            # Compare identical layer indexes
            for layer_idx, (c_state, m_state) in enumerate(zip(clean_states, misleading_states)):
                sim = compute_tensor_cosine_similarity(c_state, m_state)
                records.append({
                    "model": m_name,
                    "problem_id": prob["id"],
                    "layer": layer_idx,
                    "cosine_similarity": sim
                })
                
        del harness
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            
    df_act = pd.DataFrame(records)
    df_act.to_csv("results/internal_similarities.csv", index=False)
    return df_act
