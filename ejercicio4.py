from typing import Union

from fastapi import FastAPI

app = FastAPI()

#Creacion ruta para saludo por nombre
@app.get("/saludo/{nombre}")
def read_name(nombre: Union[str, None] = None):
    return {"Hello": nombre}

#Creacion ruta para calculadora (suma)
@app.get("/calculadora/suma")
def read_suma(num1: int, num2: int):
    return {"Resutado suma": num1 + num2}