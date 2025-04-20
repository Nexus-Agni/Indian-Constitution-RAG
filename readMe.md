
# 📜 ConstitutionAI - Indian Constitution Question Answering System

A powerful Retrieval-Augmented Generation (RAG) based question-answering system designed to help users explore and understand the **Indian Constitution** using **LLMs** with context-aware responses.

---

## 🧠 Project Overview

ConstitutionAI allows users to ask questions about the Indian Constitution and receive step-wise, data-backed answers. The system uses:

- **LangChain** for document processing
- **Google's Gemini (via OpenAI SDK)** as the LLM
- **Qdrant** as the vector store for retrieval
- **RAG** to ensure context-aware, reference-based generation

---

## 📁 File Structure

```bash
.
├── main.py                # Entry point of the application
├── LLM_calling.py         # Handles interaction with the Gemini LLM
├── RAG.py                 # Loads and processes the Indian Constitution PDF, manages vector storage & retrieval
├── Indian-Constitution.pdf  # (Place your PDF here)
```

---

## 🚀 How It Works

1. **User Input**: The user enters a question.
2. **RAG Processing**:
   - The system loads the Indian Constitution from PDF.
   - It splits the document into chunks.
   - Vector embeddings are generated using Google Generative AI Embeddings.
   - Qdrant vector store is used to retrieve the most relevant content based on the user query.
3. **LLM Interaction**:
   - The query and retrieved context are sent to Gemini.
   - The model follows a strict prompt template with reasoning steps: **Understand → Analyse → Think → Conclude**
   - Only Constitution-related queries are allowed; others are rejected with a domain message.

---

## 💡 Features

- 🔍 Context-aware Q&A using actual Constitution references
- 📘 Page numbers for traceable source citation
- 🔐 Domain-restricted LLM (only accepts legal/constitutional questions)
- 💬 Multi-step reasoning approach for each response
- 💾 Qdrant integration for efficient vector search

---

## 🔧 Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <https://github.com/Nexus-Agni/Indian-Constitution-RAG.git>
   cd <Indian-Constitution-RAG>
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file or export your Google API key:
   ```bash
   export GOOGLE_API_KEY=your_google_api_key
   ```

4. **Run the app**:
   ```bash
   python main.py
   ```

---

## 🧱 Tech Stack

- **Python**
- **LangChain**
- **Google Generative AI**
- **OpenAI SDK**
- **Qdrant Vector DB**
- **PDF Parsing (PyPDFLoader)**



