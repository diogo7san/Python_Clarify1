#-------- Etapa 1 --------
# Qual o seu nome
nome = input('Qual o seu nome? ')
# Que ano nasceu
ano_nascimento = int(input('Qual o ano em que você nasceu? '))
# Que ano estamos
ano_atual = int(input('Qual o ano vigente? '))
# Print -> Quantos anos o usuário tem como resultado
print(f'{nome}, você tem {ano_atual - ano_nascimento} ano(s)!')

teste = input('Você gostaria de testar de novo: \n[1] Sim \n[2] Não\n')

while teste == "1":
    nome = input('Qual o seu nome? ')
    ano_nascimento = int(input('Qual o ano em que você nasceu? '))
    ano_atual = int(input('Qual o ano vigente? '))
    print(f'{nome}, você tem {ano_atual - ano_nascimento} ano(s)!')
    teste = input('Você gostaria de testar de novo: \n[1] Sim \n[2] Não\n')
    if teste == "2":
        print("Tudo bem! Quando precisar, estarei aqui 😃")

##-------- Etapa 2 --------
# Toda vez que dar o resultado, perguntar: Você quer fazer de novo? Resposta: Sim, Não
# Se disser que Não, o programa termina.

#-------------------------------------------------------------------
#Pegar o código no GitHub do Caio



#https://servicodados.ibge.gov.br/api/docs/