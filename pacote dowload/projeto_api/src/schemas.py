from pydantic import BaseModel, Field, field_validator

class ListaValores(BaseModel):
    valores: list[float] = Field(
        ...,
        min_length=1,
        json_schema_extra={
            "example":{"valores":[1.0, 2.0, 3.0]}
        }
    )
    @field_validator("valores")
    def validar_desvio(cls, v):
        if len(v) >= 2 and len(set(v)) == 1:
            raise ValueError("valores não podem ser todos iguais")
        return v

class DoisVetores(BaseModel):
    vetor_a: list[float] = Field(..., min_length=1)
    vetor_b: list[float] = Field(..., min_length=1)

    @field_validator("vetor_b")
    def validar_tamanho(cls, v, info):
        vetor_a = info.data.get("vetor_a")
        if vetor_a and len(v) != len(vetor_a):
            raise ValueError("Vetores devem ter o mesmo tamanho")
        return v

