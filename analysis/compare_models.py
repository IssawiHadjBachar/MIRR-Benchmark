import pandas as pd

def compute_research_findings():
    df_b = pd.read_csv("results/behavioral_metrics.csv")
    df_r = pd.read_csv("results/reasoning_similarity.csv")
    df_a = pd.read_csv("results/internal_similarities.csv")
    df_rawr = pd.read_csv("results/right_answer_wrong_reason.csv")
    
    print("\n" + "="*50 + "\n AUTOMATED RESEARCH FINDINGS REPORT \n" + "="*50)
    
    acc = df_b.groupby(["model", "condition"])["correct"].mean().unstack()
    print("\n[Finding 1] Accuracy across Conditions:")
    print(acc.to_string())

    mean_sim = df_r.groupby("model")["reasoning_similarity"].mean()
    print("\n[Finding 2] Average Reasoning Similarity (Clean vs Misleading):")
    print(mean_sim.to_string())
    
    print(f"\n[Finding 3] Detected Right-Answer Wrong-Reason cases: {len(df_rawr)}")
    if len(df_rawr) > 0:
        print(df_rawr[["model", "problem_id", "reasoning_similarity"]].to_string())
        
    mean_act = df_a.groupby(["model", "layer"])["cosine_similarity"].mean().reset_index()
    print("\n[Finding 4] Max Activation Layer Drift (Lowest Cosine Similarity):")
    for model in mean_act["model"].unique():
        sub = mean_act[mean_act["model"] == model]
        idx_min = sub["cosine_similarity"].idxmin()
        row = sub.loc[idx_min]
        print(f" Model: {model} -> Layer {int(row['layer'])} with Mean Similarity: {row['cosine_similarity']:.4f}")
    print("="*50)
