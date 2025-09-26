def calculadora_ir(salario_bruto):
    tabela_ir = [
        {'faixa':(0,1903),           'aliquota':0,    'deducao':0},
        {'faixa':(1904,2826),        'aliquota':7.5,  'deducao':142},
        {'faixa':(2827,3751),        'aliquota':15, '  deducao':354},
        {'faixa':(3752,4664),        'aliquota':22.5, 'deducao':636},
        {'faixa':(4665,float("inf")),'aliquota':27.5, 'deducao':869}
    ]
    imposto = 0
    for nivel in tabela_ir:
        if salario_bruto > nivel["faixa"][0] and salario_bruto <= nivel["faixa"][1]:
            imposto = (salario_bruto * nivel ["aliquota"]) / 100 - nivel["deducao"]
            break
    return imposto

    #Reserva de Espaço

salario_bruto = float(input("Informe seu salário bruto: \n"))
imposto = calculadora_ir(salario_bruto)
print(f"O imposto de renda devido é de R$ {imposto}")
salario_liquido = salario_bruto - imposto #importante declarar a variável, ao invés de fazer a conta dentro da string.
print(f"Seu salário líquido é {salario_liquido}")