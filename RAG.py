from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
import os
from openai import OpenAI
import json
from qdrant_client import QdrantClient

google_api_key = os.getenv("GOOGLE_API_KEY")

pdf_path = Path(__file__).parent / "Indian-Constitution.pdf"

def RAG_application(query):
    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200
    )

    split_docs = text_splitter.split_documents(documents=documents)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=google_api_key
    )

    qdrant_client = QdrantClient(url='http://localhost:6333')
    collection_name = 'Constitution-RAG'

    if qdrant_client.get_collection(collection_name):
        vector_store = QdrantVectorStore.from_existing_collection(
            embedding=embeddings,
            url='http://localhost:6333',
            collection_name= 'Constitution-RAG'
        )
    else : 
        vector_store = QdrantVectorStore.from_documents(
        documents=split_docs, 
        embedding=embeddings,
        url='http://localhost:6333',
        collection_name = 'Constitution-RAG'
    )

    # vector_store = QdrantVectorStore.from_documents(
    #     documents=split_docs, 
    #     embedding=embeddings,
    #     url='http://localhost:6333',
    #     collection_name = 'Constitution-RAG'
    # )

    print("📝📝📝📝📝📝📝📝-----RAG processed-----📝📝📝📝📝📝📝")

    retriever = vector_store.from_existing_collection(
        embedding=embeddings,
        url='http://localhost:6333',
        collection_name= 'Constitution-RAG'
    )

    RAG_search_result = retriever.similarity_search(
        query=query
    )

    context_text = " ".join(
        [f"Page {doc.metadata['page']}: {doc.page_content}" for doc in RAG_search_result]
    )

    return context_text
