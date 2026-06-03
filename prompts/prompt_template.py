def build_prompt(question: str) -> str:
    return f"""
          You are a reasoning assistant.

          Solve the problem step by step.

          Return your response EXACTLY in this format:

          Reasoning:
          <your reasoning>

          Final Answer:
          <answer only>

          Question:
          {question}
          """
