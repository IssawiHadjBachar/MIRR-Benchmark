import os
import pandas as pd
import torch
from data.prompts import BENCHMARK_DATASETS
from models.model_harness import ModelHarness
from evaluation.answer_extraction import extract_final_answer, normalize_and_compare

def run_behavioral_pipeline(model_names: list, prompt_template_fn) -> pd.DataFrame:
    records = []
    os.makedirs("results", exist_ok=True)
    
    for m_name in model_names:
        try:
            harness = ModelHarness(m_name)
        except Exception as e:
            print(f"Skipping model {m_name} due to execution error: {e}")
            continue
            
        for prob in BENCHMARK_DATASETS:
            for condition in ["clean", "hinted", "misleading"]:
                raw_prompt = prob[condition]
                formatted_prompt = prompt_template_fn(raw_prompt)
                
                print(f"Generating: Model={m_name}, ID={prob['id']}, Condition={condition}")
                response = harness.generate_response(formatted_prompt)
                pred_answer = extract_final_answer(response)
                is_correct = normalize_and_compare(pred_answer, prob["answer"])
                
                records.append({
                    "model": m_name,
                    "problem_id": prob["id"],
                    "condition": condition,
                    "response": response,
                    "predicted_answer": pred_answer,
                    "expected_answer": prob["answer"],
                    "correct": is_correct
                })
                
       
        del harness
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            
    df = pd.DataFrame(records)
    df.to_csv("results/behavioral_metrics.csv", index=False)
    return df
