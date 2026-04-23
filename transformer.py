from sentence_transformers import SentenceTransformer
from memory import Memory


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
        self.model: SentenceTransformer = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def compare(self, memory1: Memory, memory2: Memory) -> float:
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
        similarities = self.model.similarity(memory1.embedding, memory2.embedding)

        # similarities[0][0] extracts the cosine similarity between sentence1 and sentence2
        difference = similarities[0][0]

        return float(difference)

    def encode(self, query: str):
        return self.model.encode(query, convert_to_tensor=True)

    def sort_by_relevance(self, memories: list[Memory], query: str):
        # TODO: add docstring
        query_embedding = self.encode(query)
        query_memory = Memory(content=query, embedding=query_embedding, importance=1)
        memories.sort(key=lambda m: self.compare(query_memory, m), reverse=True)


if __name__ == "__main__":
    # Example usage:
    t = Transformer()
