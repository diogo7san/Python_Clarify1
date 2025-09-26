#Vai acabar com os teus erros.
#Tente ler isso, não deu certo? Faça outra coisa que é garantida que vai dar certo!
def divisao(a,b):
    try:
        # tente fazer isso
        resultado = a / b
        print(f"O resultado da divisão de {a} e {b} é: {resultado}")

    except ZeroDivisionError:
        # erro de divisão por erro
        print("Erro: Tentou dividir por 0? Tá errado rapaz!")

    except TypeError:
        # erro de tipo
        print("Errro: Não dá pra dividir textos")

    except Exception as descricao:
        # captura qualquer erro que não pensamos
        print(f"É um erro Inesperado: {descricao}")

    else:
        #só se tudo der certo
        print("Divisão realizada com sucessso")

    finally:
        #sempre é executado, com erro
        print("Processo de devisão concluido!")

    #except TimeoutError:
    #Não dá pra programar sem Try e Except.
    #Batch

divisao(10,2)
divisao(10,0)
divisao(10,"dois")
divisao("10",2)