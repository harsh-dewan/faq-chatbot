import os
import json
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

with open("faqs.json", "r") as f:
    data = json.load(f)

training_data = [f"Q: {item['question']} A: {item['answer']}" for item in data["questions"]]

dataEmbeddings = OpenAIEmbeddings(openai_api_key=openai_key)
vectordb = Chroma.from_texts(training_data, dataEmbeddings, persist_directory="db")
vectordb.persist()

print("Successfully ingested FAQs data into ChromaDB from JSON")
