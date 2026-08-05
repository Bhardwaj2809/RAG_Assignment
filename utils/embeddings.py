from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            "BAAI/bge-base-en-v1.5"
        )

        print("Embedding model loaded.\n")

    def encode(self, text):

        return self.model.encode(
            text,
            normalize_embeddings=True,
        ).tolist()