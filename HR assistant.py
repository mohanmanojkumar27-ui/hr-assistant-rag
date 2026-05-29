import chromadb
import os
from pypdf import PdfReader
from dotenv import load_dotenv
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
import requests
load_dotenv()
api = os.getenv("Gemini_API_Key")
emb=DefaultEmbeddingFunction()
url="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
reader=PdfReader(r"C:\Users\Manoj\OneDrive\Desktop\projects\month_3\Terms_Of_Employment.pdf")
full_text=""
for page in reader.pages:
    full_text+= page.extract_text()
client=chromadb.PersistentClient(path="./storage")
collection=client.get_or_create_collection(name='HR_docs',
embedding_function=emb,
metadata={"hnsw:space":"cosine"}
)
chunk_size=500
chunks=[]
for i in range(0,len(full_text),chunk_size):
    chunk=full_text[i:i+chunk_size]
    if chunk:
        chunks.append(chunk)
if collection.count() == 0:
    collection.add(
        ids=[str(i) for i in range(len(chunks))],
        documents=chunks,
        metadatas=[{"source":"Terms_Of_Employment","page":i} for i in range(len(chunks))]
    )
past_collection=client.get_or_create_collection(name='questions',
embedding_function=emb)
name=input('Hi I am your assistant, may i know your name')
print(f"Nice to meet you {name}!.\n")
c=0
while True:
    question=input('ask me your question or enter "exit"')
    if question.lower()== "exit":
        print(f"you have asked {c} questions thanks")
        break
    results=collection.query(query_texts=[question],n_results=3)
    context="\n".join(results["documents"][0])
    que=[]
    que.append(question)
    if past_collection.count()>0:
        past_results=past_collection.query(query_texts=[question],n_results=1)
        distance = past_results["distances"][0][0]
        if distance < 0.3:
            print("You already asked this!")
            continue
    prompt = f"""
    Context: {context}
    Question: {question}
    """
    response = requests.post(url, headers={"Content-Type": "application/json", "x-goog-api-key": api},
    json={"systemInstruction": {"parts": [{"text": "You are a helpful assistant. Answer only from the provided context. If answer is not in context say I don't know. Think step by step."}]},
    "contents": [{"parts": [{"text": prompt}]}]})
    data = response.json()
    try:
        answer = data["candidates"][0]["content"]["parts"][0]["text"]
    except:
        answer = "Sorry, something went wrong. Please try again."
    print(answer)
    c += 1
    past_collection.add(
        ids=[str(c)],
        documents=[question]
    )


