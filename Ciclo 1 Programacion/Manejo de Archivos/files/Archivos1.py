import pickle

'''with open('data.txt', 'r') as f:
    data = f.read()
    print (data)
'''
#COMO ABRIR UN ARCHIVO
#FUNCION OPEN RECIBE COMO PRIMER PARAMETRO LA RUTA Y EL SEGUNDO EL MODO DE APERTURA, EL ARCHIVO QUEDARA ABIERTO HASTA QUE YO LO CIERRE
#'r' LO ABRE EN MODO LECTURA
#EL with CIERRA AUTOMATICAMENTE EL ARCHIVO PORDENTRO DE SU BLOQUE DE CODIGO
#as f ASIGNA F COMO VARIABLE PARA ALMACENAR EL ARCHIVO
#LA FUNCION read LEE TODO LO QUE ESTA EN EL ARCHIVO Y QUEDA COMO CADENA DE CARACTERES
#"W"
'''
with open('wdata2.txt', 'w') as f:
    data = "Estamos escribiendo\n"
    f.write(data)
    f.write(data)
'''
#'r' lee, 'w' Crea un archivo y escribe sobre el, si ya existe, lo reemplaza con otro
#'a' escribe al final de un archivo ya existente
#EL PUNTERO POR DEFECTO INICIA AL COMIENZO DEL ARCHIVO EN READ, EN a EL PNTERO SE UBICA AL FINAL
#SI A f.read(N), N VA A SER EL NUMERO DE CARACRTERES QUE VA A LEER, VA A MOVER EL PUNTERO HASTA AHI
#readline() LEE LA LINEA DE DONDE ESTA EL PUNTERO (CURSOR) Y QUEDA EN LA ULTIMA POSICION DE LA LINEA

#PONER TODAS LAS LINEAS EN UNA LISTA
'''
with open('wdata.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    print(data)
'''
#PROCESAR ARCHIVOS DE MANERA EFICIENTE
#ITERAR SOBRE EL ARCHIVO
'''
for linea in f:
    print(linea, end = "")
'''
#COMO ESCRIBIR EN UN ARCHIVO
#write  SOLO ESCRIBE CADEDNAS DE CARACTERES, HAY QUE CONVERTIR TODO A str()

#FUNCION seek(ESTUDIARLO, MIJO, DE VERDAD ESTUDIELO): UBICA EL CURSOR EN UNA POSICION DETERMINADA DEL ARCHIVO
#FUNCION tell() ME DICE EL TAMAÑO EN BYTES DEL ARCHIVO
#EDITAR LINEAS DEL ARCHIVO
#EL MODULO os SIRVE PARA INTERACTUAR CON EL OS EN ESTE CASO LISTAR,ELIMINAR CREAR Y ETC 
#MODULO pickle:
#ALMACENA EN UN ARCHIVO ESTRUUCTURAS DE DATOS DE PYTHON

lista = {80:"HTTPS", 22:"SSH"}
tupla = ("LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES")
with open("diccionario.pkl", "wb") as f:
    pickle.dump(lista, f) #SERIALIZACION, BUSCAR QUE ES
    pickle.dump(tupla, f) 

with open("diccionario.pkl", 'rb') as f:
    a = pickle.load(f) #CARGO MI LISTA EN LA VARIABLE
    b = pickle.load(f)

print(a)
print(b)

#COPIAR UN ARCHIVO DE UNA UBICACION A OTRA
with open('discurso.jpg', 'rb') as f:
    data = f.read()

print(data)
with open('discurs_copy.jpg', 'wb') as f:
    f.write(data)
