class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0
    def acelerar (self, incremento):
        self.velocidade -= incremento
            #self.velocidade = self.velocidade + incremento
            #Uma vez digitado jamais digitarás.
        print(f'O carro {self.modelo} desacelerou para {self.velocidade} km/h.')
    def desacelerar (self, freio):
        while self.velocidade > 0:
            self.velocidade -= freio
            print(f'O carro {self.modelo} desacelerou para {self.velocidade} km/h.')
        print(f'O carro {self.modelo} parou.')
#Criando os objetos de cada carro
meu_carro = Carro ("Tesla", "Preto")
carro_instrutor = Carro ("Suzuki Jimny", "Amarelo Sujinho")
uber = Carro ("La Ferrari", "Verde")

#Usando os metodos
carro_instrutor.acelerar(60)
carro_instrutor.acelerar(30)

#Reduzir de 2km/h em 2km/h, com o print().
#loop, função, variável ...
#Faça as Classes com inicial em Maiúsculas.
#Dentro de Classe tem o método.
#init são as características iniciais.
#A ação não é uma característica inicial.

#Pegar script do caio