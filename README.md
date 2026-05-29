# HR Assistant RAG 🤖

A RAG-based HR assistant that answers questions from company PDF documents using ChromaDB and Gemini API.

## What it does
- Reads a PDF document
- Stores it in ChromaDB vector database
- Answers questions using Google Gemini API
- Only answers from the document, not from internet
- Detects duplicate questions using semantic similarity

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
