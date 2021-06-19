#JSON
#TODAS LAS CLAVES SON CADENAS DE CATACTERES
import json
import requests
from pprint import pprint
#EJEMPLO

'''
{
    "Nombre":"Douglas",
    "Apellido":"Crockford",
    "Pasatiempos":["Trotar", "Bucear", "Cantar"]
    "Edad":64
    "Empleado":false
    "Jefe":null
    "Hijos":[
        {"Nombre":"Alice", "Edad": 19
        "Nombre": "Bob"  }
    ]
}
'''
#UN OBJETO JSON CASI SIEMPRE SE PUEDE TRADUCIR A UN DICCIONARIO EN PYTHON
data = {
    "cientifico": {
        "nombre": "Alan Mathison Turing",
        "edad": "41"
    }
}
print(data)
#SERIALIZACION, SE HACE PARA CONVERTIR UNA ESTRUCTURA EN UN JSON
#MANERA 1
#TRADUCE A JSON EL DICCIONARIO DE PYTHON
with open("json/data.json", "w") as f:
    json.dump(data, f)

#TAMBIEN PODEMOS LEERLO, Y GUARDARLO EN UN STRING (SERIALIZACION A TEXTO)
json_string = json.dumps(data)
print(type(json_string))

#SEGUNDA MANERA DE SERIALIZAR (IDENTAR)
json_string = json.dumps(data, indent=4) #EL 4 ES LA CANIDAD DE ESPACIOS CON EL QUE INDENTA
print(json_string)

#DESERIALIZACION (LO CONTRARIO, OBJETOS JSON A ESTRUCTURA DE DATOS EN PYTHON)
with open("json/data.json", "r") as f:
    deserealizacion = json.load(f) #LOAS CON S ES PARA STRINGS Y MULTILINEA
print(type(deserealizacion), deserealizacion)
#SI DESEREALIZO JSON ANIDADOS, EN PYHON SERAN LISTAS O ESTRUCTURAS ANIDADAS TAMBIEN

strjson = '''{
"boolean1": null,
"diccionario": {"papa": 2000, "arroz": 5000},
"intValue": 0, "myList": [],
"myList2":["info1", "info2"],
"littleboolean": false, "myEmptyList": null,
"text1": null, "text2": "hello", "value1": null,
"value2": null}'''
data = json.loads(strjson)
pprint(data) #SIRVE PARA IMPRIMIR MAS ORDENADAMENTE LA ESTRUCTURA

#OBTEBER JSON DESDE INTERNET
response = requests.get("https://jsonplaceholder.typicode.com/todos")
pendientes = json.loads(response.text)

pprint(type(pendientes))

#NANEJAR O FILTRAR COSAS DE LAS LISTAS
conteo = {}
for tarea in pendientes:
    if tarea["completed"]:
        if tarea["userId"] in conteo:
            conteo[tarea["userId"]] +=1
        else:
            conteo[tarea["userId"]] = 1

print(conteo)

#ORDENAR
print(list(conteo.items()))
items_ordeados = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
print(items_ordeados)