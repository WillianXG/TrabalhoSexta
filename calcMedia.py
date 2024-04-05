def calcularMediaAluno():
    while True:
        nota1 = float(input("Digite a primeira nota do aluno: "))
        nota2 = float(input("Digite a segunda nota do aluno: "))
        
        if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
            media = (nota1 + nota2) / 2
            break
        else:
            print("\nErro! As notas devem estar entre 0 e 10.\n")

    if media >= 0 and media <= 4:
        return 'Conceito E'
    elif media > 4 and media <= 6:
        return 'Conceito D'
    elif media > 6 and media <= 7.5:
        return 'Conceito C'
    elif media > 7.5 and media <= 9:
        return 'Conceito B'
    elif media > 9 and media <= 10:
        return 'Conceito A'
    else:
        return 'Média Inválida'

print(calcularMediaAluno())


#pronto