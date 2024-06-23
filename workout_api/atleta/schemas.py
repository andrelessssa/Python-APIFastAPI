from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated

class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do Atleta', examples='Joao', max_lengyh=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', examples='12345678912', max_lengyh=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', examples='25')]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', examples='70.5' )]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', examples='1.70')]
    sexo: Annotated[str, Field(description='Sexo do Atleta', examples='M', max_lengyh=1)]