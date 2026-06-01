from fastapi import FastAPI, HTTPException, Query
from src.schemas import ListaValores, DoisVetores
from src.algorithms import media, mediana, desvio_padrao, distancia, resumo

app = FastAPI(
    title="API Estatística Descritiva",
    description="API para cálculo de métricas estatísticas como média, mediana, desvio padrão e operações com vetores.",
    version="1.0.0"
)

@app.get("/")
def health():
    return {"status": "ok", "versao": "1.0.0"}

@app.post("/estatisticas/media", tags=["Estatísticas"])
def calc_media(dados: ListaValores):
    try:
        return {"media": media(dados.valores)}
    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno")

@app.post("/estatisticas/mediana", tags=["Estatísticas"])
def calc_mediana(dados: ListaValores):
    return {"mediana": mediana(dados.valores)}

@app.post("/estatisticas/desvio-padrao", tags=["Estatísticas"])
def calc_dp(dados: ListaValores):
    if len(dados.valores) < 2:
        raise HTTPException(status_code=400, detail="mínimo 2 valores")
    return {"desvio_padrao": desvio_padrao(dados.valores)}

@app.post("/estatisticas/resumo", tags=["Estatísticas"])
def calc_resumo(dados: ListaValores, decimais: int = Query(2, ge=0, le=6)):
    r = resumo(dados.valores)

    for k in r:
        r[k] = round(r[k], decimais)

    return r

@app.post("/vetores/distancia", tags=["Vetores"])
def calc_distancia(dados: DoisVetores):
    if len(dados.vetor_a) != len(dados.vetor_b):
        raise HTTPException(status_code=400, detail="tamanhos diferentes")
    return {"distancia": distancia(dados.vetor_a, dados.vetor_b)}

@app.post("/vetores/escalar/{valor}", tags=["Vetores"])
def escalar(valor: float, dados: ListaValores):
    return {"resultado": [x * valor for x in dados.valores]}
