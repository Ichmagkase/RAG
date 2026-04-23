from unsloth import FastLanguageModel


class Model:
    def __init__(self):
        self.model, self.tokenizer = FastLanguageModel.from_pretrained(
            model_name="unsloth/Llama-3.2-1B-Instruct",
            max_seq_length=2048,
            load_in_4bit=True,  # keeps memory usage low
        )
        FastLanguageModel.for_inference(self.model)

    def prompt(self, query: str) -> str:
        messages = [{"role": "user", "content": query}]
        # inputs = self.tokenizer(query, return_tensors="pt").to("cuda")
        inputs = self.tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt",
            return_dict=True,
        ).to("cuda")
        input_length = inputs["input_ids"].shape[1]
        outputs = self.model.generate(**inputs, max_new_tokens=256, max_length=None)
        return self.tokenizer.decode(
            outputs[0][input_length:], skip_special_tokens=True
        )
