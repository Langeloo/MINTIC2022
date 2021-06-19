#   ESTRUCTURA FOR SE SUPONE QUE PROPIAMENTE NO SE USA ASI
suma = 0
n = 15
for i in range(1, n, 1):
    print(i)
#SE USA CON COLECCIONES
'''
for <elemento> in <coleccion> :
    <bloque>
<bloque siguiente>
'''
#FOR QUE RECORRA UNA LISTA DE FRUTAS
frutas = ["Peras", "Manzanas", "Tomate de arbol",
          "Maracuya", "Guayaba", 12, 123.89]
for i in frutas:
    print(i)
    if i == "Peras":
        print("Que puto xd")
print(frutas.__contains__("Maracuya"))

#EL BREAK EN ESTE CASO SE VERIA MEJOR PARA PARAR EL CICLO
#EXISTE UN RANGO VACIO, PARA RANGOS IMPOSIBLES
#ASI LO SIMPRIME SEGUIDOS Y EN LLAVES
r = range(0, 10)
print(list(r))
n = int(input('Cuantos numeros quiere sumar?: '))
sum = 0
for c in range(0, n + 1):
    sum += c
print(sum)
#FUNCIONA COMO n * (n + 1) / 2  FUNCIONA XD, LA SUMA DE LOS N NATURALES
