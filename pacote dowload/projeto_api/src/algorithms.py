import math

def media(valores):
    return sum(valores) / len(valores)

def mediana(valores):
    valores = sorted(valores)
    n = len(valores)
    meio = n // 2
    if n % 2 == 0:
        return (valores[meio - 1] + valores[meio]) / 2
    return valores[meio]

def desvio_padrao(valores):
    m = media(valores)
    variancia = sum((x - m) ** 2 for x in valores) / len(valores)
    return math.sqrt(variancia)

def distancia(v1, v2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

def variancia(valores):
    m = media(valores)
    return sum((x - m) ** 2 for x in valores) / len(valores)

def resumo(valores):
    return {
        "media": media(valores),
        "mediana": mediana(valores),
        "minimo": min(valores),
        "maximo": max(valores),
        "amplitude": max(valores) - min(valores),
        "variancia": variancia(valores), 
        "desvio_padrao": desvio_padrao(valores)
    }
    