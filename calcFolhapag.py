def calculoFolhaPagamento():
    horas_trabalhadas = float(input("Quantas horas você trabalhou este mês?\n>> "))
    valor_hora = float(input("Qual é o valor da sua hora de trabalho?\n>> "))

    salario_bruto = horas_trabalhadas * valor_hora
    ir = 0
    
    if salario_bruto <= 900:
        ir = 0
    elif salario_bruto <= 1500:
        ir = 0.05
    elif salario_bruto <= 2500:
        ir = 0.1
    else:
        ir = 0.2

    desconto_ir = salario_bruto * ir
    desconto_sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    total_descontos = desconto_ir + desconto_sindicato
    salario_liquido = salario_bruto - total_descontos

    print("\nFOLHA DE PAGAMENTO")
    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"(-) IR ({ir * 100}%): R$ {desconto_ir:.2f}")
    print(f"(-) Sindicato (3%): R$ {desconto_sindicato:.2f}")
    print(f"FGTS (11%): R$ {fgts:.2f}")
    print(f"Total de descontos: R$ {total_descontos:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

calculoFolhaPagamento()
