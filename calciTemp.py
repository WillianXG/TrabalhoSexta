def calcularTemperaturas():
    temperaturas = []
    ponto_de_parada = False

    while not ponto_de_parada:
        temperatura = float(input("Digite a temperatura atual (para encerrar, digite -999): "))
        
        if temperatura == -999:
            ponto_de_parada = True
        else:
            temperaturas.append(temperatura)

    if temperaturas:  # Verifica se a lista de temperaturas não está vazia
        menor_temperatura = min(temperaturas)
        maior_temperatura = max(temperaturas)
        media_temperatura = sum(temperaturas) / len(temperaturas)

        return f'Menor Temperatura: {menor_temperatura}\nMaior Temperatura: {maior_temperatura}\nMédia: {media_temperatura}\n'
    else:
        return "Nenhuma temperatura foi informada."

print(calcularTemperaturas())
