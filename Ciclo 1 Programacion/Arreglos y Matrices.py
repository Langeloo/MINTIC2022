#ES UNA TUPLA O LISTA DE N ELEMENTOS DEL MISMO TIPO
#LEER ARREGLOS
def leer_arreglos_enteros():
    return [int(x) for x in input("Arreglo: ").split(" ")]

#SUMAR ELEMENTOS DE UN ARREGLO
arreglo = leer_arreglos_enteros()
arreglo.sort()
print(arreglo[len(arreglo) - 1])