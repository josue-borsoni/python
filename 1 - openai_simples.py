from openai import OpenAI

import os                       # Para carregar o arquivo .env com a chave da api
from dotenv import load_dotenv  # Para carregar o arquivo .env com a chave da api
load_dotenv() # Carrega o arquivo .env com a chave da api

linguagem = "java"

prompt = f"Escreva um resumo sobre a linguagem de programação {linguagem}"
print(prompt)

cliente = OpenAI( api_key = os.getenv("OPENAI_API_KEY"))

resposta = cliente.chat.completions.create( model="gpt-3.5-turbo",
                                            messages=[
                                                {"role": "system", "content": "Você deve se comportar como um doutor em PHD"},
                                                #{"role": "system", "content": "Você deve se comportar como uma criança"},
                                                {"role": "user", "content": prompt}
                                            ])

conteudoExibir = resposta.choices[0].message.content

print(conteudoExibir);
