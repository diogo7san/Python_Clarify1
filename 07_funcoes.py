nome = input('Qual seu nome?:\n')
horario = int(input ('Que horas são? (24H):\n'))
repeticoes = int(input('Quantas vezes deseja executar?'))

if horario <= 12:
    saudacao = "Bom dia"
elif horario <= 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

def montarFrase(texto01, texto02):
    print(f"{texto01} {texto02}, be happy 😃")

ligar = True
contador = 0
while ligar:
    montarFrase(saudacao, nome)
    contador = contador + 1
    if contador >= repeticoes:
        ligar = False



