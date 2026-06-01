# API de Estatística Descritiva

## Descrição
API de Estatística Descritiva - endpoints computacionais que recebem dados numéricos, calculam e retornam resultados. Sem persistência, sem CRUD. Cada requisição é autocontida (stateless).

## Funcionalidades
* Cálculo de média
* Cálculo de mediana
* Cálculo de desvio padrão
* Resumo estatístico completo
* Distância euclidiana entre vetores
* Multiplicação de vetor por escalar

## Tecnologias
* Python
* FastAPI
* Pydantic
* Pytest

## Como executar
### 1. Criar ambiente virtual
```
python -m venv .venv
```

### 2. Ativar ambiente
```
.venv\Scripts\activate
```

### 3. Instalar dependências
```
pip install -r requirements.txt
```

### 4. Rodar a API
```
python -m uvicorn src.api:app --reload
```

## Acessar documentação
```
http://127.0.0.1:8000/docs
```

## Rodar testes
```
python -m pytest
```

## Estrutura do projeto
```
src/
    api.py
    algorithms.py
    schemas.py
tests/
    test_algorithms.py
    test_api.py
requirements.txt
README.md
requests.http
```
