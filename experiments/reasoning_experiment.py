import pandas as pd
from evaluation.reasoning_similarity import ReasoningEvaluator

def run_reasoning_similarity_pipeline() -> pd.DataFrame:
    df_behavioral = pd.read_csv("results/behavioral_metrics.csv")
    evaluator = ReasoningEvaluator()
    
    models = df_behavioral["model"].unique()
    prob_ids = df_behavioral["problem_id"].unique()
    records = []
    
    for model in models:
        for p_id in prob_ids:
            clean_rows = df_behavioral[(df_behavioral["model"] == model) & 
                                      (df_behavioral["problem_id"] == p_id) & 
                                      (df_behavioral["condition"] == "clean")]
            misleading_rows = df_behavioral[(df_behavioral["model"] == model) & 
                                           (df_behavioral["problem_id"] == p_id) & 
                                           (df_behavioral["condition"] == "misleading")]
            
            if not clean_rows.empty and not misleading_rows.empty:
                clean_text = clean_rows.iloc[0]["response"]
                misleading_text = misleading_rows.iloc[0]["response"]
                
                similarity = evaluator.compute_similarity(clean_text, misleading_text)
                records.append({
                    "model": model,
                    "problem_id": p_id,
                    "reasoning_similarity": similarity
                })
                
    df_sim = pd.DataFrame(records)
    df_sim.to_csv("results/reasoning_similarity.csv", index=False)
    return df_sim
