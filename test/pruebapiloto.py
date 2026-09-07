#1) Crear base de datos con nombres.
#2) Crear una lista con opciones.
#3) Crear un input para poner el nombre de la serie y que lo busque en la base de datos.
#4) Me tiene que devolver un mensaje si lo encuentra o no.

import json

print("Bienvenido a SeriesPlay")
print("Elija su opción:")
print("1) Buscar serie")
print("2) Salir")
print("=======================================)")
opcion = input("Opción: ")

if opcion == "1":
    def leer_series():
        nombre_serie = input("Ingrese el nombre de la serie que desea buscar: ")
        with open("dataset_1000.json") as f:
            data = json.load(f)
            for nombre_serie in data["series"]:
                print(f"La serie ["title"] se encuentra en la base de datos.")
            else:
                print(f"La serie ["title"] no se encuentra en la base de datos.")
    
    
elif opcion == "2":
    print("Gracias, vuelvas prontos")

else:
    print("Opción inválida")
