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
        inputs = self.tokenizer(query, return_tensors="pt").to("cuda")
        outputs = self.model.generate(**inputs, max_new_tokens=256)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
