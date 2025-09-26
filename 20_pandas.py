#Sempre que usar com dados use o Pandas pra manipular
#O Pandas cria um manipulador chamado dataframe (estrutura dos dados)
#É o excel pra Python
#pip install pandas
#O Pandas faz o tratamento dos dados como no Excel
import pandas as pd
data = {
    "Nome": ["Juliana", "Byanca", "Diogo", "Marcelo", "Emanuel", "Horacio" ],
    "Idade": [12, 22, 32, 44, 45, 21],
    "Salario": [ 5000,6000,7000,8000,9000,4000]
}
#Não importa de onde veio, eu posso transformar dados em dataframe.

df = pd.DataFrame(data)

print("Conteúdo do Dataframe:")
print(df)

#Selecionado apenas uma coluna
print("\n Coluna de nome: ")
print(df["Nome"])

#Filtrando linhas
print("\n Pessoas com idade menor que 30")
print(df[df["Idade"] < 30])

#Calculando imposto e adicionando uma nova coluna
df["Imposto"] = df["Salario"] * 0.1
print("\n Nova coluna de imposto")
print(df)

media_salarial = df['Salario'].mean()
print("\n Média Salarial: ")
print(media_salarial)

#Salvando o dataframe em um arquivo CSV
df.to_csv(r"C:\Users\integral\Desktop\pythonDiogo\salarios.csv", index=False)

leitura = pd.read_csv(r"C:\Users\integral\Desktop\pythonDiogo\salarios.csv")

print("\nTabela importada do arquivo CSV: ")
print(leitura)