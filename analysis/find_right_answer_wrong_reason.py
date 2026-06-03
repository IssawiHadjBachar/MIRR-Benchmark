import pandas as pd

def find_anomalous_behavior() -> pd.DataFrame:
    df_behavioral = pd.read_csv("results/behavioral_metrics.csv")
    df_reasoning = pd.read_csv("results/reasoning_similarity.csv")

    misleading_correct = df_behavioral[(df_behavioral["condition"] == "misleading") & 
                                       (df_behavioral["correct"] == True)]

    merged = pd.merge(misleading_correct, df_reasoning, on=["model", "problem_id"])

    candidates = merged[merged["reasoning_similarity"] < 0.50]
    
    output_cols = [
        "model", "problem_id", "predicted_answer", 
        "expected_answer", "reasoning_similarity", "response"
    ]
    candidates = candidates[output_cols]
    candidates.to_csv("results/right_answer_wrong_reason.csv", index=False)
    return candidates
