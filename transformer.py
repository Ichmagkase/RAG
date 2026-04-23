from sentence_transformers import SentenceTransformer


class Transformer:
    def __init__(self):
        # 1. Load a pretrained Sentence Transformer model
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def compare(self, sentence1, sentence2):
        embeddings = self.model.encode([sentence1, sentence2])
        similarities = self.model.similarity(embeddings, embeddings)
        difference = similarities[0][0] - similarities[0][1]

        return abs(difference)


if __name__ == "__main__":
    # Example usage:
    t = Transformer()
    print(t.compare("I walked my dog yesterday", "I own a cat"))
    print(t.compare("I walked my dog today", "dogs like to eat dog food"))
