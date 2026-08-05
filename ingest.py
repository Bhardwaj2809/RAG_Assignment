import uuid
from tqdm import tqdm
from qdrant_client.models import PointStruct

from utils.pdf_loader import load_pdfs
from utils.chunker import chunk_text
from utils.embeddings import EmbeddingModel
from utils.qdrant_db import QdrantDB

PDF_FOLDER = "pdfs"
BATCH_SIZE = 100


def main():

    print("=" * 60)
    print("        PDF INGESTION")
    print("=" * 60)

    # Load embedding model
    embedding_model = EmbeddingModel()

    # Connect to Qdrant
    db = QdrantDB()

    # Load PDFs
    documents = load_pdfs(PDF_FOLDER)

    print(f"\nLoaded {len(documents)} pages.\n")

    # Create collection
    vector_size = len(embedding_model.encode("hello"))

    db.create_collection(vector_size)

    batch = []
    total_chunks = 0

    print("Generating embeddings...\n")

    for document in tqdm(documents):

        chunks = chunk_text(document["text"])

        for chunk in chunks:

            vector = embedding_model.encode(chunk)

            batch.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=vector,
                    payload={
                        "document": document["document"],
                        "page": document["page"],
                        "text": chunk,
                    },
                )
            )

            total_chunks += 1

            # Upload every 100 chunks
            if len(batch) >= BATCH_SIZE:
                db.insert(batch)
                batch = []

    # Upload remaining chunks
    if batch:
        db.insert(batch)

    print("\n" + "=" * 60)
    print(f"Finished!")
    print(f"Uploaded {total_chunks} chunks.")
    print("=" * 60)


if __name__ == "__main__":
    main()