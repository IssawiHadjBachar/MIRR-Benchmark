# Mechanistic Interpretability & Reasoning Robustness Benchmark

## Overview
This project evaluates how language models behave under clean, hinted, and misleading reasoning prompts.  
It analyzes not only final answers but also the consistency of reasoning processes across conditions.

The study focuses on:
- Behavioral accuracy
- Reasoning consistency (semantic similarity)
- Internal activation stability
- Right-Answer-Wrong-Reason (RAWR) detection

The project was fully developed and executed using Google Colab.

---

## Models Evaluated
- Qwen/Qwen2.5-0.5B-Instruct  
- EleutherAI/pythia-410m  

---

## Project Structure
- `data/` → benchmark reasoning dataset  
- `models/` → model loading + generation pipeline  
- `evaluation/` → similarity + answer extraction  
- `experiments/` → behavioral, reasoning, activation analysis  
- `analysis/` → plots + aggregated results  
- `results/` → outputs and figures  

---

## Methodology

### 1. Behavioral Evaluation
Each model is tested under three conditions:
- Clean prompt
- Hinted prompt
- Misleading prompt

Metrics:
- Accuracy per condition

---

### 2. Reasoning Similarity
We compute semantic similarity between explanations using Sentence-BERT embeddings.

This allows us to measure how stable the model’s reasoning is across conditions.

### Threshold-Based Filtering
We isolate specific failure cases using the rule:

Isolate targets matching the threshold rule: reasoning similarity < 0.50

This helps identify cases where the model’s reasoning significantly diverges under perturbations.

---

### 3. Activation Similarity
We extract transformer hidden states and compute cosine similarity between clean and misleading conditions.

This measures how internal representations shift under adversarial prompts.

---

### 4. RAWR Detection
We detect Right-Answer-Wrong-Reason (RAWR) cases where:
- The final answer is correct
- But the reasoning differs significantly

---

## Key Results Interpretation

### Accuracy
Models perform better with hints but degrade under misleading prompts, showing strong prompt sensitivity.

### Reasoning Similarity
Higher similarity indicates stable explanation patterns, but does not necessarily imply correct reasoning.

### Activation Similarity
High similarity suggests that internal representations remain stable even under perturbations.

### RAWR Cases
No strong RAWR patterns were detected, likely due to:
- Small dataset size
- Limited reasoning diversity

---

## Limitations
- Small dataset (~10 problems)
- Only two models evaluated
- Greedy decoding used (no sampling diversity)
- No supervised chain-of-thought control

---

## Future Work
- Expand to larger and stronger models
- Add more reasoning benchmarks
- Attention pattern analysis
- Adversarial prompt generation
- Improve RAWR detection sensitivity

---

## Reproducibility
All experiments were run in Google Colab.