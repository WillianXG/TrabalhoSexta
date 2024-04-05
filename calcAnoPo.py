def calcularAnosIgualarPopulacao():
    populacao_a = 80000
    populacao_b = 200000
    anos = 0

    while populacao_a < populacao_b:
        populacao_a *= 1.03
        populacao_b *= 1.015
        anos += 1

    return f'Serão necessários {anos} anos para a população do país A alcançar ou ultrapassar a população do país B.'

print(calcularAnosIgualarPopulacao())
