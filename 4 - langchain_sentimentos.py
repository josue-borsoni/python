from langchain_openai  import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains  import LLMChain # Executa uma coisa
from langchain.chains  import SimpleSequentialChain # Executa uma sequancia de passos
from langchain.globals import set_debug # para ter mais informaç~eos ainda sobre o debug
import os                       # Para carregar o arquivo .env com a chave da api
from dotenv import load_dotenv  # Para carregar o arquivo .env com a chave da api

load_dotenv() # Carrega o arquivo .env com a chave da api
#sset_debug(True)

#Cria a LLM que será utilizada, neste caso a llm da OpenAi, gpt-3.5-turbo
var_llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY"))

#Criar os prompts
prompt_identificar_core   = PromptTemplate.from_template("Identificar o core do comentário: {comentario}. Retorne apenas o core.")
prompt_analise_sentimento = PromptTemplate.from_template("Analisar sentimento e classificar com notas entre 1 e 10. Analisar do {core}")

cadeia_identificar_core   = LLMChain(llm = var_llm, prompt = prompt_identificar_core)
cadeia_analise_sentimento = LLMChain(llm = var_llm, prompt = prompt_analise_sentimento)

#Executa os prompts de forma encadeada
cadeia_sequencial = SimpleSequentialChain(chains = [cadeia_identificar_core, cadeia_analise_sentimento])

resultado = cadeia_sequencial.invoke("O uniforme de desfle do time brasil era muito bnito");  #bonito feio normal joga

print(resultado)