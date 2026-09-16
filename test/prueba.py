# funcion que cargue y retorne los datos

import json

ruta_archivo = "dataset_10.json"
def cargar_json(ruta_archivo):
    with open(ruta_archivo) as f:
        datos = json.load(f)
    return datos

print(cargar_json(ruta_archivo)["series"][2]["title"])