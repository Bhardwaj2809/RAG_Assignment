def chunk_text(text, chunk_size=800, overlap=150):
    """
    Splits text into overlapping chunks.

    Example

    Chunk 1
    ----------------------
    0 -------- 800

             overlap

    Chunk 2
    ----------------------
          650 --------1450
    """

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks