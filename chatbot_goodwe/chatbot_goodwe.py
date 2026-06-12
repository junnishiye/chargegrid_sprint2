%pip install --quiet --upgrade langchain-text-splitters langchain-community langgraph langchain-openai langchain-core pypdf unstructured

# configuração chatgpt
import getpass
import os
from google.colab import userdata
from langchain.chat_models import init_chat_model
from langchain_core.vectorstores import InMemoryVectorStore

os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')
llm = init_chat_model("gpt-4o-mini", model_provider="openai")

#selecionando o embedding
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

vector_store = InMemoryVectorStore(embeddings)

from google.colab import drive
drive.mount('/content/drive')

import shutil
import os

destino = "/content/drive/MyDrive/chatbot_docs"
os.makedirs(destino, exist_ok=True)

arquivos = [
    "/content/GW_HCA-G2_User-Manual-PT.pdf",
    "/content/goodwe_carregador.pdf",
    "/content/GoodWe_EV_ChargeOps_Base_Conhecimento.pdf",
    "/content/goodwe_instalacao.pdf",
    "/content/goodwe_manualcarregador.pdf",
    "/content/goodwe_manualdousuario.pdf",
    "/content/goodwe_carregador1.pdf",
    "/content/chatbot.pdf"
]

for arquivo in arquivos:
  if os.path.exists(arquivo):
    shutil.move(arquivo, destino)

print("Arquivos movidos com sucesso!")

#base de cohecimento do chatbot
import bs4
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader

BASE_PATH = "/content/drive/MyDrive/chatbot_docs/"

file_path1 = BASE_PATH + "goodwe_manualdousuario.pdf"
file_path2 = BASE_PATH + "goodwe_carregador.pdf"
file_path3 = BASE_PATH + "goodwe_carregador1.pdf"
file_path4 = BASE_PATH + "goodwe_instalacao.pdf"
file_path5 = BASE_PATH + "goodwe_manualcarregador.pdf"
file_path6 = BASE_PATH + "GW_HCA-G2_User-Manual-PT.pdf"
file_path7 = BASE_PATH + "GoodWe_EV_ChargeOps_Base_Conhecimento.pdf"
file_path8 = BASE_PATH + "chatbot.pdf"

loader1 = PyPDFLoader(file_path1)
loader2 = PyPDFLoader(file_path2)
loader3 = WebBaseLoader(["https://br.goodwe.com/"])
loader4 = PyPDFLoader(file_path3)
loader5 = PyPDFLoader(file_path4)
loader6 = PyPDFLoader(file_path5)
loader7 = PyPDFLoader(file_path6)
loader8 = PyPDFLoader(file_path7)
loader9 = PyPDFLoader(file_path8)

docs1 = loader1.load()
docs2 = loader2.load()
docs3 = loader3.load()
docs4 = loader4.load()
docs5= loader5.load()
docs6 = loader6.load()
docs7 = loader7.load()
docs8 = loader8.load()
docs9 = loader9.load()

docs = docs1 + docs2 + docs3 + docs4 + docs5 + docs6 + docs7 + docs8 + docs9

docs

#splitting dos documentos
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # chunk size (characters)
    chunk_overlap=200,  # chunk overlap (characters)
    add_start_index=True,  # track index in original document
)
all_splits = text_splitter.split_documents(docs)

print(f"Split pdf into {len(all_splits)} sub-documents.")

all_splits[0]

#guardando os dados em um banco de dados
document_ids = vector_store.add_documents(documents=all_splits)

print(document_ids[:3])

from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, AIMessage
from typing_extensions import List, TypedDict

# memória do chatbot
chat_history = []

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

def retrieve(state: State):

    retrieved_docs = vector_store.similarity_search(
        state["question"]
    )

    return {"context": retrieved_docs}

def generate(state: State):

    global chat_history

    docs_content = "\n\n".join(
        doc.page_content
        for doc in state["context"]
    )

    historico = "\n".join([
        f"Usuário: {msg.content}"
        if isinstance(msg, HumanMessage)
        else f"Assistente: {msg.content}"
        for msg in chat_history
    ])

    prompt_final = f"""
Você é um assistente especializado nos produtos GoodWe.

Use APENAS as informações do contexto fornecido.
Se não encontrar a resposta no contexto, diga que não encontrou na base.

Histórico da conversa:
{historico}

Contexto:
{docs_content}

Pergunta:
{state["question"]}

Resposta:
"""


    response = llm.invoke(prompt_final)


    chat_history.append(
        HumanMessage(content=state["question"])
    )


    chat_history.append(
        AIMessage(content=response.content)
    )

    return {"answer": response.content}


from langgraph.graph import START, StateGraph

graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

result = graph.invoke({"question": "Qual é a função do administrador nesse processo"})

print(f'Context: {result["context"]}\n\n')
print(f'Answer: {result["answer"]}')

print(chat_history)

result
