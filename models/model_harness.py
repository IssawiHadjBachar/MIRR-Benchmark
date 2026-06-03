import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class ModelHarness:
    def __init__(self, model_name: str):
        self.model_name = model_name
        print(self.model_name)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Loading {model_name} on {self.device}...")
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto" if self.device == "cuda" else None,
            trust_remote_code=True
        )
        if self.device == "cpu":
            self.model.to(self.device)
            
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def generate_response(self, text_prompt: str, max_new_tokens: int = 512) -> str:
        """Generates a standard text output response from the model."""
        inputs = self.tokenizer(text_prompt, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                temperature=None,
                top_p=None,
                top_k=None,
                pad_token_id=self.tokenizer.pad_token_id
            )
       
        input_len = inputs['input_ids'].shape[1]
        return self.tokenizer.decode(outputs[0][input_len:], skip_special_tokens=True)

    def get_layer_representations(self, text_prompt: str) -> list:

      inputs = self.tokenizer(
          text_prompt,
          return_tensors="pt"
      ).to(self.device)

      with torch.no_grad():
          outputs = self.model(
              **inputs,
              output_hidden_states=True
          )

      hidden_states = [
          layer_state[0]
          .mean(dim=0)
          .detach()
          .cpu()
          .to(torch.float32)
          for layer_state in outputs.hidden_states
      ]

      return hidden_states
