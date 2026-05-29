# HR Assistant RAG 🤖

An AI-powered HR assistant built with RAG (Retrieval Augmented Generation) that answers employee policy questions from company documents-without hallucinating or going outside the provided context.

## What it does
- Reads a PDF document
- Stores it in ChromaDB vector database
- Answers questions using Google Gemini API
- Only answers from the document, not from internet
- Detects duplicate questions using semantic similarity

## How it works
1. Extracts text from PDF using PyPDF2
2. Splits into 500 character chunks
3. Stores chunks in ChromaDB with embeddings
4. User asks a question
5. Retrieves top 3 relevant chunks using cosine similarity
6. Gemini generates answer from retrieved context only

## Tech used
- Python
- ChromaDB
- Google Gemini API
- PyPDF2

## How to run
1. Clone the repo
2. Add your Gemini API key to .env file: Gemini_API_Key=your_key
3. Add your PDF to the folder
4. Run: python "HR assistant.py"
