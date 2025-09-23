nomeCompleto =  "Diogo Pereira de Santana"
inicio = 5
fim = inicio + 6
print(nomeCompleto[inicio:fim]) #O início é contado a partir do 0, e o fim do 1.

nome = input("Qual o seu nome? ")
sobrenome = input("Informe seu sobrenome completo ")
print("Seu nome é " + nome + " " + sobrenome) #Em um web scraping, por exemplo, se usa um valor a ser inserido para você não ter que mexer no código.

valor01 = input('Insira seu primeiro valor: ') #Poderia colocar int aqui: int(input('...))
valor02 = input('Insira seu segundo valor: ') #Tudo do imput vem como texto

valor01 = int(valor01)

print(valor01 + int(valor02))

