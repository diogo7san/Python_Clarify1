"""Trabalhando com tipos e variáveis"""

nome = "Diogo"
sobrenome = "Pereira de Santana"
outronome = nome
idade = 38 #valor inteiro
altura = 1.81
bermuda = False #boolean
calca = True

# exibir o conteúdo da variável
print(nome)
# print(nome + " " + sobrenome + "tem" + idade + " anos.") #Espaço aumenta a elegibilidade.
# + não é pra concatenar, é pra somar.
print(nome + " " + sobrenome + " tem" + str(idade) + " anos.")

print(idade + 2)

textoVariasLinhas = '''
uma linha
outra linha
mais uma
'''
print(textoVariasLinhas)
