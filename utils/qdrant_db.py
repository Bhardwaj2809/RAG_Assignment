import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

load_dotenv()

COLLECTION_NAME = os.getenv("COLLECTION_NAME", "legal_documents")


class QdrantDB:

    def __init__(self):

        self.client = QdrantClient(
            host=os.getenv("QDRANT_HOST", "localhost"),
            port=int(os.getenv("QDRANT_PORT", "6333"))
        )

    def create_collection(self, vector_size):

        collections = self.client.get_collections().collections

        existing = [c.name for c in collections]

        if COLLECTION_NAME not in existing:

            self.client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE
                )
            )

            print(f"Collection '{COLLECTION_NAME}' created.")

        else:

            print(f"Collection '{COLLECTION_NAME}' already exists.")

    def insert(self, points):

        self.client.upsert(
            collection_name=COLLECTION_NAME,
            wait=True,
            points=points
        )

    def search(self, vector, limit=5):

        results = self.client.search(
            collection_name=COLLECTION_NAME,
            query_vector=vector,
            limit=limit
        )

        if len(results) == 0:
            return []

        # Ignore unrelated results
        if results[0].score < 0.65:
            return []

        return results