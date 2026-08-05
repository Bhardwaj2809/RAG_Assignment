# AI Python Engineering Assignment - RAG Application

## Overview

This project implements a Retrieval-Augmented Generation (RAG) application that answers user questions using only the provided PDF documents.

The application extracts text from PDFs, generates embeddings using Sentence Transformers, stores them in Qdrant Vector Database, retrieves relevant chunks based on the user's question, and generates answers using an OpenRouter free LLM.

Every answer includes citations containing:

- Document Name
- Page Number
- Retrieved Text Snippet

If the answer is not found in the supplied documents, the application returns:

> "The information is not available in the supplied documents."

---

## Architecture

PDFs

↓

PDF Loader

↓

Chunking

↓

Sentence Transformer Embeddings

↓

Qdrant Vector Database

↓

Similarity Search

↓

OpenRouter LLM

↓

Answer + Citations

---

## Libraries Used

- Python 3.12
- PyMuPDF
- Sentence Transformers
- Qdrant Client
- Requests
- python-dotenv
- tqdm

---

## Embedding Model

BAAI/bge-base-en-v1.5

---

## LLM

google/gemma-3-9b-it:free

---

## Assumptions

- All PDF documents are placed inside the `pdfs/` folder.
- Docker is used to run a local Qdrant instance.
- OpenRouter API key is required.

---

## How to Run

```bash
docker compose up -d
```

```bash
pip install -r requirements.txt
```

```bash
python ingest.py
```

```bash
python app.py
```
