from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_media():
    r = client.post("/estatisticas/media", json={"valores":[1,2,3]})
    assert r.status_code == 200
    assert r.json()["media"] == 2

def test_mediana():
    r = client.post("/estatisticas/mediana", json={"valores":[1,2,3]})
    assert r.status_code == 200
    assert r.json()["mediana"] == 2

def test_desvio_padrao():
    r = client.post("/estatisticas/desvio-padrao", json={"valores":[2,4,6,8]})
    assert r.status_code == 200

def test_resumo():
    r = client.post("/estatisticas/resumo", json={"valores":[1,2,3,4]})
    assert r.status_code == 200
    assert "media" in r.json()

def test_lista_vazia():
    r = client.post("/estatisticas/media", json={"valores":[]})
    assert r.status_code == 422

def test_distancia():
    r = client.post("/vetores/distancia", json={
        "vetor_a":[0,0],
        "vetor_b":[3,4]
    })
    assert r.status_code == 200
    assert r.json()["distancia"] == 5

def test_vetor_invalido():
    r = client.post("/vetores/distancia", json={
        "vetor_a":[1,2],
        "vetor_b":[1]
    })
    assert r.status_code == 422

def test_escalar():
    r = client.post("/vetores/escalar/2", json={
        "valores":[1,2,3]
    })
    assert r.status_code == 200
    assert r.json()["resultado"] == [2,4,6]
