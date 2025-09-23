
tipoEscola = input("Estuda em colégio: \n [1] Publico\n[2]Particular\n")
nomeAluno = input("Qual o nome do aluno?\n")
mediaAluno = int(input("Qual a média do aluno " + nomeAluno+ "?\n"))
freqAluno = int(input("Qual a frequencia do aluno " + nomeAluno + "?\n"))

#float não se usa em dinheiro
'''
!= diferente
== igual
<= menor ou igual
>= maior ou igual
< menor
> maior
'''
if tipoEscola == "2":
    print("---------------- Escola Particular ----------------")
    if mediaAluno >= 7 and freqAluno >= 70: #Esqueça o sinal de %
        status = "Aprovado"
    else:
        status = "Reprovado"

if tipoEscola == "1":
    print("---------------- Escola Pública ----------------")
    if mediaAluno >= 6 or freqAluno >= 70:
        status = "Aprovado"
    else:
        status = "Reprovado"

#print ("O aluno " + nomeAluno + " foi " + status + " com média " + mediaAluno)
print (f"O aluno {nomeAluno} foi {status} com média {mediaAluno}")