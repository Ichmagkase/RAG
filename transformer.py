from sentence_transformers import SentenceTransformer


class Transformer:
    """A wrapper for generating and comparing sentence embeddings.

    This class utilizes the `sentence-transformers` library to load a
    pretrained model and provides a simplified interface for comparing
    the semantic meaning of two text strings.

    Attributes:
        model (SentenceTransformer): The loaded pretrained MiniLM model used
            for generating embeddings.
    """

    def __init__(self):
        """Initializes the Transformer by loading the pretrained model."""
        # 1. Load a pretrained Sentence Transformer model
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def compare(self, sentence1: str, sentence2: str) -> float:
        """Calculates the cosine similarity between two sentences.

        This method encodes both sentences into vector space and computes
        their semantic similarity. It extracts the raw similarity score,
        where a score closer to 1.0 means the sentences are highly similar,
        and a score closer to 0.0 means they are largely unrelated.

        Args:
            sentence1 (str): The first text string to compare.
            sentence2 (str): The second text string to compare.

        Returns:
            float: The absolute cosine similarity score between the two vectors.
        """
        embeddings = self.model.encode([sentence1, sentence2])
        similarities = self.model.similarity(embeddings, embeddings)

        # similarities[0][1] extracts the cosine similarity between sentence1 and sentence2
        difference = similarities[0][1]

        return float(difference)


if __name__ == "__main__":
    # Example usage:
    t = Transformer()

    # Expected: Lower similarity score
    print("Similarity 1:", t.compare("I walked my dog yesterday", "I own a cat"))

    # Expected: Higher similarity score (due to shared dog context)
    print(
        "Similarity 2:", t.compare("I walked my dog today", "dogs like to eat dog food")
    )
