from src.algorithms import media, mediana, desvio_padrao, distancia, resumo

def test_media():
    assert media([1, 2, 3]) == 2

def test_mediana_impar():
    assert mediana([1, 2, 3]) == 2

def test_mediana_par():
    assert mediana([1, 2, 3, 4]) == 2.5

def test_desvio_padrao():
    resultado = desvio_padrao([2, 4, 6, 8])
    assert round(resultado, 2) == 2.24

def test_distancia():
    assert distancia([0, 0], [3, 4]) == 5

def test_resumo():
    r = resumo([1, 2, 3, 4])
    assert r["media"] == 2.5
    assert r["minimo"] == 1
    assert r["maximo"] == 4
    