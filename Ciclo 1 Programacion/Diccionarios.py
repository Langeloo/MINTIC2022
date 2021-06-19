#PAREJA CLAVE VALOR
#EJEMPLOñ CEDULA, LA LLAVE VA A SER UNICA EN EL CONJUNTO
#EN PYTHON SE ESCRIBE clave:valor
#UNA VEZ ASIGNO LA CLVE, NO PUEDE SER MUTABLE
#ES BASICAMENTE UNA COLECCION DESORDENADA, EN LAS DEMAS ESTRUCTURAS DE DATOS EXISTE UN ORDEN ESTABLECIDO

puertos = {80: "HTTP", 22: "SSH", 443: "HTTPS",
           23: "Telnet", "llave": [1, 2, 3]}
print(type(puertos))
print(puertos)  # NO TIENEN ORDEN ESPECIFICO, NO TIENEN SUBINDICES
#SI HAY DOS LLAVES IGUALES, SOLO GUARDARA LA ULTTIMA QUE ESCRIBIMOS, SOBREESCRIBE EL VALOR

puertos2 = {53: "DNS", 5432: "Postgres"}
#funcion-metodo UPDATE
puertos.update(puertos2)
print(puertos)
#AGREGA AL FINAL EL DICCIONARIO QUE LE ENVIE EN LA FUNCION

#COMPARAR DICCIONARIOS
puertos3 = {53: "DNS", 5432: "Postgres"}
# ES IGUAL PORQUE TITNTN LAS MISMAS LLAVES Y VALORES
print(puertos3 == puertos2)

datos = {"Nombre": "Juan", "Edad": 29, "Apellido": "Castro"}
print(datos["Nombre"])

#AGREGAR NUEVOS ELEMENTOS A UN DICCIONARIO
datos["Edad"] = 30
print(datos["Edad"])  # ACTUUALIZACION DE DATOS

#AGREGAR NUEVA PAREJA LLAVE:VALOR
datos["Direccion"] = "Calle falsa xd"  # SOLO DEFINIMOS LA NUEVA PAREJA
print(datos)

#ELIMINAR UN ELEMENTO (PAREJA LLAVE:VALOR)
del datos["Direccion"]  # SI NO PONE LA LLAVE, LE ELIMINA TODO EL DICCIONARIO
print(datos)

#BUSCAR SOBRE DICCIONARIO
if 80 in puertos:
    print("SI")
else:
    print("NO")

print(80 in puertos)

#ITERAR SOBRE DICCIONARIOS
for key in puertos:
    print(key)  # TRAE O ITERA SOBRE LAS LLAVES, NO SOBRE LAS CLAVES
#FORMA 2, TRAER TODA LA PAREJA
for key in puertos.items():
    print(key)
#TRAER EN PRINTS
for key, pws in puertos.items():  # ASIGNACION MULTIPLE DE VARIABLES
    print(key, " -> ", pws)
#ESTO ES UNA PRUEBA, TRAER LAS CLAVES Y NO LAS LLAVES
for key in puertos:
    print(puertos[key])

#METODOS PARA DICCIONARIOS
print(len(puertos))  # CUANTAS PAREJAS LLAVE-VALOR EXISTEN
#FORMAS DE TRAER UN DATO
print(puertos[443])
# CUANDO LA LLAVE NO EXISTE, EL SEGUNDO PARAMETRO ES UN VALOR POR DEFECTO++
print(puertos.get(43, "Como que no existe"))

#MIN Y MAX
print(min(datos))
print(max(datos))  # TRAE EL MINIMO Y MAXIMO DE LAS LLAVES

#OBTENER LOS DATOS EN UNA LISTA
print(list(datos.keys()))
print(list(datos.values()))

#CONVERTIR A DICCIONARIOS
#LA LISTA DE LISTAS DEBE CONTENER LISTAS DE DOS ELEMENTOS, tambien funciona con tuplas, intercambiable (creo)
lista = [[80, "http"], [443, "Https"], [22, "SSH"]]
dict1 = dict(lista)
print(dict1)

#ELIMINAR ENTRADAS
print(datos.clear())  # ELIMINA TODO EL DICCIONARIO, NO SE PUEDE REESTABLECER

#COPIAR DICCIONARIOS
puertos_copy = puertos.copy()
puertos_copy_2 = puertos

print(puertos_copy)
print(puertos_copy_2)

puertos_copy[238] = "New"
puertos[000] = "New_2"
print(puertos_copy)
#CUANDO USO COPY HACE UNA COPIA EN DIFERENTE ESPACIO DE MEMORIA, PERO CUANDO USO = CAMBIAN LAS DOS PORQUE APUNTAN AL MISMO ESPACIO DE MEMORIA
