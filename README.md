# E-Commerce FAQ Chatbot with OpenAI + ChromaDB

A hands-on **Retrieval-Augmented Generation (RAG)** project that answers FAQ-style questions using:
- **OpenAI embeddings** for semantic vectorization  
- **ChromaDB** for vector search (retrieval)  
- **GPT-4o-mini** for natural language answers  
- **FastAPI** backend for deployment  

This project demonstrates how real-world AI/ML developers **integrate embeddings, vector databases, and LLMs** to build data-driven applications.

---

## Features
- Semantic search → understands meaning, not just keywords  
- Dataset-only mode → won’t hallucinate answers if info isn’t present  
- FastAPI endpoint → query via browser, Swagger UI, or Postman  
- Modular pipeline → easily swap OpenAI with HuggingFace embeddings, or GPT with LLaMA
- Dataset Source: https://www.kaggle.com/datasets/saadmakhdoom/ecommerce-faq-chatbot-dataset/data

---

## Tech Stack
- **LangChain** → pipeline management  
- **OpenAI** → embeddings + LLM  
- **ChromaDB** → vector storage & retrieval  
- **FastAPI** → API server  
- **Python-dotenv** → environment management  

---

## Project Structure
faq-chatbot/
- ├── app.py # FastAPI app with /ask endpoint
- ├── ingest.py # Ingests FAQs into ChromaDB
- ├── faqs.json # FAQ dataset
- ├── requirements.txt
- ├── .env # API key
- ├── db/ # Vector DB (ignored by git)


---

## How It Works
1. **Ingest phase** → `ingest.py` reads `faqs.json`, generates embeddings with OpenAI, stores them in ChromaDB.  
2. **Query phase** → User sends a query to `/ask`.  
3. **Retrieval** → Query is embedded and compared against stored vectors in ChromaDB.  
4. **LLM answer** → Retrieved FAQs are passed to GPT-4o-mini, which summarizes into a clean answer.  

---

## Setup & Run

## 1. Clone repo & install dependencies

git clone https://github.com/harsh-dewan/faq-chatbot.git
cd faq-chatbot
pip install -r requirements.txt

## 2. Add API key
Update .env file with API key
OPENAI_API_KEY=sk-xxxx

## 3. Ingest FAQs
python ingest.py

## 4. Run FastAPI server
python -m uvicorn app:app --reload



## Screenshots & Examples

## Screenshot showing GET request + returned answer


## Example 1
<img width="858" height="521" alt="image" src="https://github.com/user-attachments/assets/499766e6-f8fe-47ef-a8c1-e747f7b8d162" />



## Example 2
<img width="856" height="514" alt="image" src="https://github.com/user-attachments/assets/a72d1ea8-0381-4e21-b38f-e08b9bfae6db" />



## Example 3
<img width="869" height="527" alt="image" src="https://github.com/user-attachments/assets/00b646cb-6d2c-4a7a-9aeb-08a6e879b777" />




## Example 4
<img width="868" height="493" alt="image" src="https://github.com/user-attachments/assets/e2f1352c-c7cc-4acd-90d9-515c0b405333" />




## Example 5
<img width="812" height="535" alt="image" src="https://github.com/user-attachments/assets/cf401582-2b41-4604-89c0-02a13bfeb5fa" />



## Extensions & Next Steps

 1. Add similarity threshold to filter weak matches
 2. Build a simple React UI on top of FastAPI
 3. Deploy on AWS/GCP with Docker + CI/CD pipeline





