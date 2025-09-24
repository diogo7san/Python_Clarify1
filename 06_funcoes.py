def minhaFuncao():
    print("Bom dia Python ❤️")

minhaFuncao()
minhaFuncao()
minhaFuncao()
minhaFuncao()

contador = 0
ativar = True
while ativar:
    minhaFuncao()
    contador = contador + 1
    if contador >= 10:
        ativar = False
print('terminei')


