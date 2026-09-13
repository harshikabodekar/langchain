
from langchain_text_splitters import RecursiveCharacterTextSplitter

text="""Artificial Intelligence (AI) and Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) is an architectural framework designed to improve the accuracy and reliability of Large Language Models (LLMs). Instead of relying solely on static knowledge learned during pre-training, RAG fetches relevant background context from external data sources before generating a response.

Key Components of a RAG Pipeline:

1. Document Loading: Raw documents in formats like PDF, TXT, or HTML are ingested using document loaders.
2. Text Splitting: Large documents are broken down into smaller, manageable chunks using text splitters like RecursiveCharacterTextSplitter.
3. Embedding Generation: Each text chunk is converted into a numerical vector representation using an embedding model.
4. Vector Storage: These embeddings are indexed and saved inside vector databases such as Chroma, FAISS, or Pinecone.
5. Retrieval & Generation: When a user asks a question, the system retrieves the most relevant text chunks from the vector database and passes them alongside the prompt to the language model.

By combining private enterprise data with powerful foundation models, RAG reduces hallucinations and enables real-time information retrieval without costly model fine-tuning."""
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    #separator=' ')
)

chunks =text_splitter.split_text(text)
print(chunks)
