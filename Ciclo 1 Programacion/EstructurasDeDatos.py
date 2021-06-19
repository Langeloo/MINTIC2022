#ESTRUCTURAS DE DATOS

#CADENAS O CONJUNTOS DE  CARACTERES

print('hola \n mundo') #\n ES UN SALTO DE LINEA EN UNICODE (CARACTER DE CONTROL)
print('hola \t mundo') #\t ES UNA TABULACION
print("Imprimir estos tipos de comillas" + '" "'+" y "+"' '")
print("Tambien se puede asi \"  \'")
print("Imprimir \\") #SE PONEN DOS PARA QUE IMPRIMA 1
print("\u01a9") #IMPRIME EN UNICODE
c = "12"
d = int(c)
m = d+2
print(m)

#  COMPARACIONES ENTRE CADENAS
print('Rosas' < "Rojas")
cadena = "Cadena de caracteres"
print("Primer caracter: " + cadena[0] + " Ultimo caracter: " + cadena[-1])
buscar = "dena"
print(cadena.__contains__(buscar))
print("SI") if "dena" in cadena else print("NO")
#LA CADENA VACIA SIEMPRE ESTA EN TODAS LAS CADENAS

print(cadena.split(" "), sep=", ")
for c in cadena:
    print(c, end=", ")
print(cadena.count("d"))
print(len(cadena))
#TOMAR CADENAS POR PARTES O POR RANGOS
print(cadena[2:5])
print(cadena[3:12:2])
print(cadena[:5])
print(cadena[5:])
print(cadena[:-2])
#LA FUNCION find DEVUELVE EL INDICE DONDE ESTA UN CARACTER, SOLO LA PRIMERA VEZ QUE LO ENCUENTRA Y rfind DEVUELVE LA ULTIMA OCURRENCIA
print(cadena.find("na"))
print(cadena.rfind("os"))  # DA -1 SI NO ENCUENTRA NADA
#lower() pone todo en minuscula upper() en mayuscula, capitalice, pasa la primera a mayuscula
#title() cambia a mayuscula la primera de cada palabra
#strip/lstrip/lstrip esta remueve los caracteres que deseemos de una cadena
cadena2 = "-=-=-=-=-=-= Hola ==-=-=-=-=---=-="
print(cadena2.strip("-="))
print(cadena2.lstrip("-="))
print(cadena2.rstrip("=-"))

#el split pone cada delimitacion en una lista de tal manera que la podaoa usar con subindices
cadena3 = cadena2.split(" ")
print(cadena3)
#JUSTIFICADO DE CADENAS
print(cadena.ljust(30, "-"))
print(cadena.rjust(30, "-"))
print(cadena.center(30, "-"))
print(cadena.zfill(40))
#REPLACE REMPLAZA UNA PARTE DE LA CADENA POR OTRA
print(cadena.replace("Cadena", "Arreglo").replace("de", "con"))
