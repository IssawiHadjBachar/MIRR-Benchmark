import torch

def compute_tensor_cosine_similarity(tensor_a: torch.Tensor, tensor_b: torch.Tensor) -> float:
    cos = torch.nn.CosineSimilarity(dim=0, eps=1e-6)
    return float(cos(tensor_a, tensor_b).item())