from utils.embeddings import EmbeddingModel
from utils.qdrant_db import QdrantDB
from utils.llm import generate_answer
from utils.formatter import print_sources

print("=" * 60)
print("          LEGAL RAG ASSISTANT")
print("=" * 60)

embedding_model = EmbeddingModel()
db = QdrantDB()

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    print("\nGenerating query embedding...")

    query_vector = embedding_model.encode(question)

    print("Searching Qdrant...")

    results = db.search(query_vector)

    if len(results) == 0:

        print("\nThe information is not available in the supplied documents.\n")

        continue

    context = ""

    for result in results:

        context += f"""
Document: {result.payload['document']}
Page: {result.payload['page']}

Text:
{result.payload['text']}

----------------------------------------
"""

    print("Generating answer...\n")

    answer = generate_answer(question, context)

    print("=" * 70)
    print("ANSWER\n")
    print(answer)
    print("=" * 70)

    print_sources(results)