from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain # Executa uma coisa
from langchain.chains import SimpleSequentialChain # Executa uma sequancia de passos
from langchain.globals import set_debug # para ter mais informaç~eos ainda sobre o debug
import os                       # Para carregar o arquivo .env com a chave da api
from dotenv import load_dotenv  # Para carregar o arquivo .env com a chave da api

load_dotenv() # Carrega o arquivo .env com a chave da api
#set_debug(True)

#Cria a LLM que será utilizada, neste caso a llm da OpenAi, gpt-3.5-turbo
var_llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.5,
            api_key = os.getenv("OPENAI_API_KEY"))

#Vamos criar 3 templates. Um para sugerir Cidades, um para sugerir restaurantes e e outro para sugerir refeições em cada restaurante
modelo_cidade      = ChatPromptTemplate.from_template("Sugira uma cidade dado meu interesse por {aaa}. Retorne apenas o nome da cidade")
modelo_restaurante = ChatPromptTemplate.from_template("Sugira 10 restaurantes populares em {bbb}")
modelo_refeicao    = ChatPromptTemplate.from_template("Para cada {ccc} sugira a melhor refeição e seu respectivo valor")

#modelo_cultural    = ChatPromptTemplate.from_template("Sugira atividades e locais culturais em {cidade}")
cadeia_cidade       =  LLMChain(prompt = modelo_cidade,      llm = var_llm)
cadeia_restaurantes =  LLMChain(prompt = modelo_restaurante, llm = var_llm)
cadeia_cultural     =  LLMChain(prompt = modelo_refeicao,    llm = var_llm)

# Vamos criar uma cadeia que vai executar isto de forma sequencial
# "SimpleSequentialChain" pega o resultado da sequancia anterior e forece como input para a próxima sequência
cadeia = SimpleSequentialChain(chains = [cadeia_cidade, cadeia_restaurantes, cadeia_cultural], 
                               verbose = True)  #verbose é para passar mais informaçãoes de log do que esta acontecendo

resultado = cadeia.invoke("praias") # "praias" será o input para {interesse}

print(resultado)