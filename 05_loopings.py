palavra = "tangamandapio"
contador = 0

for letra in palavra: #programar sempre conta a partir de 0
    contador = contador + 1
    print(f"{contador} - {letra}")


cidades = ['Fortaleza', 'Belem', 'Recife', 'Poa', 'Sao Paulo']
#print(cidades[1])

for cidade in cidades:
    print(cidade)

#-------------------------------------------------------------

botaoExecutar = True
contador02 = 0

while botaoExecutar:
    print(contador02)
    contador02 = contador02 + 1
    if contador02 >= 200:
        botaoExecutar = False