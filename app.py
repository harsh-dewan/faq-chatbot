import os
from dotenv import load_dotenv

from fastapi import FastAPI
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
vectordb = Chroma(persist_directory="db", embedding_function=embeddings)
retriever = vectordb.as_retriever()
llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=openai_key)

qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, verbose=True)

@app.get("/ask")
def ask(query: str):
    docs = retriever.get_relevant_documents(query)
    for i, doc in enumerate(docs):
        print(f"Doc {i+1}: {doc.page_content}")
        break

    answer = qa.run(query)
    return {"query": query, "answer": answer}
