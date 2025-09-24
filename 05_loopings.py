palavra = "tangamandapio"
contador = 0 # contador começa em 0, mas nós vamos usá-lo como "numeração personalizada"

for letra in palavra: #programador sempre conta a partir de 0
    contador = contador + 1 # cada vez que roda, somamos +1 no contador
    # aqui imprimimos o número do contador (começa em 1) e a letra atual
    print(f"{contador} - {letra}")


cidades = ['Fortaleza', 'Belem', 'Recife', 'Poa', 'Sao Paulo']
#print(cidades[1])
# Percorrendo a lista normalmente:
for cidade in cidades:
    # Aqui a variável 'cidade' vai assumir cada valor da lista, um de cada vez
    print(cidade)

#-------------------------------------------------------------

botaoExecutar = True # variável de controle: enquanto for True, o laço continua
contador02 = 0  # contador começa em 0

while botaoExecutar: # enquanto a condição for verdadeira...
    print(contador02) # imprime o valor atual do contador
    contador02 = contador02 + 1 # incrementa o contador (soma +1)
    # condição de parada: se o contador chegar a 200 ou mais,
    # mudamos 'botaoExecutar' para False, e o laço para
    if contador02 >= 200:
        botaoExecutar = False