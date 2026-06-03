import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_and_save_plots():
    os.makedirs("results/plots", exist_ok=True)
    sns.set_theme(style="whitegrid")
    
    df_b = pd.read_csv("results/behavioral_metrics.csv")
    df_r = pd.read_csv("results/reasoning_similarity.csv")
    df_a = pd.read_csv("results/internal_similarities.csv")
    
    # Accuracy by Condition
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df_b, x="condition", y="correct", order=["clean", "hinted", "misleading"], errorbar=None, palette="viridis")
    plt.title("Overall Model Accuracy by Prompt Condition")
    plt.ylabel("Accuracy Rate")
    plt.savefig("results/plots/accuracy_by_condition.png", dpi=200)
    plt.close()
    
    # Accuracy by Model  
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df_b, x="model", y="correct", hue="condition", errorbar=None, palette="coolwarm")
    plt.title("Accuracy by Model and Condition")
    plt.xticks(rotation=15)
    plt.ylabel("Accuracy Rate")
    plt.tight_layout()
    plt.savefig("results/plots/accuracy_by_model.png", dpi=200)
    plt.close()
    
    # Mean Reasoning Similarity by Model  
    plt.figure(figsize=(7, 5))
    sns.barplot(data=df_r, x="model", y="reasoning_similarity", errorbar=None, palette="crest")
    plt.title("Mean Reasoning Similarity (Clean vs Misleading)")
    plt.xticks(rotation=15)
    plt.ylabel("Cosine Similarity")
    plt.tight_layout()
    plt.savefig("results/plots/mean_reasoning_similarity.png", dpi=200)
    plt.close()
    
    # Layer-by-Layer Activation Similarity  
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_a, x="layer", y="cosine_similarity", hue="model", marker="o")
    plt.title("Layer-by-Layer Activation Cosine Similarity (Clean vs Misleading)")
    plt.xlabel("Transformer Layer Index")
    plt.ylabel("Mean Cosine Similarity")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig("results/plots/layer_activation_similarity.png", dpi=200)
    plt.close()
    
    # Distribution of Reasoning Similarity Scores  
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df_r, x="reasoning_similarity", hue="model", kde=True, bins=10, multiple="stack", palette="magma")
    plt.title("Distribution of Reasoning Similarity Scores")
    plt.xlabel("Cosine Similarity Between Responses")
    plt.savefig("results/plots/reasoning_similarity_distribution.png", dpi=200)
    plt.close()
    
    print("All 5 required visual plots saved inside 'results/plots/'.")
