import re
from fractions import Fraction


def extract_final_answer(response_text: str) -> str:

    markers = [
        "Final Answer:",
        "final answer:",
        "FINAL ANSWER:"
    ]

    for marker in markers:
        if marker in response_text:
            answer = response_text.split(marker)[-1]

            match = re.search(
                r'[-+]?\d+(?:/\d+)?(?:\.\d+)?|yes|no',
                answer.lower()
            )

            if match:
                return match.group(0)

            return answer.strip()

    match = re.search(
        r'[-+]?\d+(?:/\d+)?(?:\.\d+)?|yes|no',
        response_text.lower()
    )

    if match:
        return match.group(0)

    return response_text.strip()


def normalize_and_compare(pred: str, expected: str) -> bool:

    p = pred.strip().lower()
    e = expected.strip().lower()

    if p == e:
        return True

    try:
        return float(Fraction(p)) == float(Fraction(e))
    except:
        pass

    return False
