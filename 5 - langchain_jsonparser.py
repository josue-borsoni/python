from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain # Executa uma coisa
from langchain.chains import SimpleSequentialChain # Executa uma sequancia de passos
from langchain.globals import set_debug # para ter mais informaç~eos ainda sobre o debug
import os                       # Para carregar o arquivo .env com a chave da api
from dotenv import load_dotenv  # Para carregar o arquivo .env com a chave da api
from langchain_core.pydantic_v1 import Field, BaseModel #para criar a nossa classe

load_dotenv() # Carrega o arquivo .env com a chave da api
set_debug(True)

class Destino(BaseModel): 
    cidade = Field("cidade a visitar")
    motivo = Field("Motivo pelo qual é interessante visitar esta cidade")


#Cria a LLM que será utilizada, neste caso a llm da OpenAi, gpt-3.5-turbo
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key = os.getenv("OPENAI_API_KEY"))

#Vamos criar 3 templates. Um para sugerir Cidades, um para sugerir restaurantes e e outro para sugerir locais
modelo_cidade      = PromptTemplate(template = "Sugira uma cidade dado meu interesse por {interesse}",  
                                    input_variable = ["interesse"])

modelo_restaurante = ChatPromptTemplate.from_template("Sugira restaurantes populares entre as pessoas locais em {cidade}")
modelo_cultural    = ChatPromptTemplate.from_template("Sugira atividades e locais culturais em {cidade}")

caeia_cidade =  LLMChain(prompt = modelo_cidade, llm = llm)
caeia_restaurantes =  LLMChain(prompt = modelo_restaurante, llm = llm)
caeia_cultural =  LLMChain(prompt = modelo_cultural, llm = llm)

# Vamos criar uma cadeia que vai executar isot de forma sequencial
# "SimpleSequentialChain" pega o resultado da sequancia anterior e forece como input para a proxima sequancia
cadeia = SimpleSequentialChain(chains=[caeia_cidade, caeia_restaurantes, caeia_cultural], 
                               verbose=True)  #verbose é para passar mais informaçãoes de log do que esta acontecendo

resultado = cadeia.invoke("praias") # "praias" será o input para {interesse}

print(resultado)