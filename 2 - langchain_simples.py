from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os                       # Para carregar o arquivo .env com a chave da api
from dotenv import load_dotenv  # Para carregar o arquivo .env com a chave da api

load_dotenv() # Carrega o arquivo .env com a chave da api


# Modelo de Prompt simples
#prompt = f"Escreva um resumo sobre a linguagem de programação {linguagem}"

# Modelo de Prompt Template
modelo_do_prompt = PromptTemplate.from_template ("Escreva um resumo sobre a linguagem {lng} e um método para calcular o {clc}")

linguagem = "c#"
calcular = "fatorial"

prompt = modelo_do_prompt.format(lng = linguagem, clc = calcular)

print(prompt)

llm = ChatOpenAI(
                model="gpt-3.5-turbo",
                temperature=0.5,
                api_key = os.getenv("OPENAI_API_KEY"))


resposta = llm.invoke(prompt);

print(resposta.content)