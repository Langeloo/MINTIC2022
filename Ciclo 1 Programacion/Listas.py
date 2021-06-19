#ESTRUCTURAS 3 //////// LISTAS
#ALMACENAN DATOS DE DIFERENTES TIPOS, INCLUSO LISTAR Y TUPLAS, CUALQUIER TIPO
#LA DIFERENCIA ENTRE LAS LISTAS ES (TUPLAS) Y [lISTAS]
#LISTAS MUTABLES: PUEDO CAMBIAR LAS LISTAS DESPUES DE QUE LAS DEFINI
'''
[]: LISTA VACIA
["ELEMENTO"]: LISTA CON UN ELEMENTO

'''
lista1 = [0, 1, 2, 3]
lista2 = ["A", "B", "C"]
#LISTAS ANIDADAS
lista3 = [lista1, lista2]
#CREAR UNA NUEVA LISTA A PARTIR DE DOS LISTAS /// CONCATENAR
lista4 = lista1 + lista2
#METODO EXTEND: AGREGA UNA LISTA A LA COLA DE LA LISTA INVOCANTE, LA CAMBIA
lista5 = lista1
lista5.extend(lista2)
#OPERADOR REPETIR
lista6 = lista1 * 3
#COMPARAR LISTAS


def comparations():
    #LOS PARES DE DATOS DEBEN SER DEL MISMO TIPO
    print(lista1 > lista1 * 2)
    print(avengers[2], avengers[4])


#SUBINDICES EN LISTAS (IMPRIMO EN LA FUNCION DE ARRIBA)
avengers = ["IRONMAN", "THOR", "ANT-MAN", "HULK", "THOR", [2, 1]]

print(type(lista6))
print(lista6)
comparations()
print(avengers.__contains__("ANT"))
#RECORRER LISTAS
for i in avengers:
    print(i)

#CREACION DE LISTAS APARTIR DE UN FOR EN UNA SOLA LINEA
d = 10
desplaza = [d + x for x in range(5)]
print(desplaza)
#ASIGNACION MULTIPLE DE LISTAS
lista7 = [1, 2, 3]
a, b, c = lista7
print(a, b, c)
#F-STRING
lista8 = [3, 5, 3, 2, 5, 6, 4, 2]
a, b = [lista8[i] for i in (2, 4)]
print(f"a: {a} b: {b} ")

base = 2
potencias_de_2 = [base**e for e in range(10)]
print(potencias_de_2)

#//////////////////////////////FUNCIONES EN LISTAS///////////////////////////
#FUNCION LEN DA NMERO DE ELEMENTOS DE LA LISTA
print(len(avengers[5]))
#FUNCION PARA CAMBIAR LOS ELEMENTOS DE UA LISTA
lista9 = [5, 3, -4, 2]
lista9[0] = 6
print(lista9)
#intercambiar variables funciona igual a,b = b,a
#AGREGAR AL FINAL DE LA LISTA
nombres = ["Antonio", "Johan"]
nombres.append("Monica")
#AGREGAR ELEMENTOS EN POSICION ESPECIFICA
nombres.insert(1, "Marcos")
print(nombres)
#ELIMINAR ELEMENTOS DE UNA LISTA
nombres.remove("Monica")  # SOLO REMUEVE LA PRIMERA APARICION
print(nombres)
#ELIMINARLOS TODOS
while "Camilo" in nombres:
    # CREO QUE HAY MAS FORMAS, COMO CONTAR CUANTOS HAY Y REMOVERLO X VECES (COUNT), O RECORRIENDO TODO
    nombres.remove("Camilo")

#SUBLISTAS
print(nombres[::2])
#CONTAR CUANTAS COINCIDENCIAS
print(nombres.count("Antonio"))
#INDEX
print(nombres.index("Antonio"))  # SOLO TRAE LA PRIMERA OCURRENCIA/
# SE PUEDEN HACER PARA TODAS
#print(nombres.index("Camilo",0,len(nombres)))
#MAX Y MIN
print(max(nombres) + " " + min(nombres))
#ORDENAR LISTAS
#ASCENDENTEMENTE
nombres.sort()
print(nombres)
#DESCENDENTEMENTE
nombres.sort(reverse=True)
print(nombres)
#CONVERTIR A LISTA OBJETOS ITERABLES
tupla1 = (1,2,3,("uno","dos"))
texto1 = "Hola mundo"
lista10 = list(tupla1)
lista11 = list(texto1)
lista12 = list(range(2, 15, 3))
print(lista10 + lista11 + lista12)
#ELIMINAR POR POSICION
lista11.pop() #SI NO HAY PARAMETRO ELIMINA EL ULTIMO, DEVUELVE EL ELEMENTO QUE ELIMINO