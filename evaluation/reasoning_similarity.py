import re

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def extract_reasoning(text: str) -> str:

    match = re.search(
        r"Reasoning:(.*?)Final Answer:",
        text,
        flags=re.S | re.I
    )

    if match:
        return match.group(1).strip()

    return text


class ReasoningEvaluator:

    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def compute_similarity(
        self,
        text_a: str,
        text_b: str
    ) -> float:

        text_a = extract_reasoning(text_a)
        text_b = extract_reasoning(text_b)

        if not text_a.strip() or not text_b.strip():
            return 0.0

        embeddings = self.model.encode(
            [text_a, text_b],
            convert_to_numpy=True
        )

        return float(
            cosine_similarity(
                [embeddings[0]],
                [embeddings[1]]
            )[0][0]
        )
