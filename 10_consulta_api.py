# import json
# import requests
# separe por contexto ou vírgula
import json, requests

nome = input("Qual o seu nome?\n")
resposta = requests.get(f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}")
#get = pegar
#toda biblioteca tem documentação, com os comandos dela.
json_dados = json.loads(resposta.text)
# tudo pro python é objeto. Objeto é algo que não só recebe a informação, mas herda propriedades.
print(json_dados[0]['res'][2])