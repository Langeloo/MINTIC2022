#ARREGLOS EN NUMPY
import numpy as np
 #AS ES PARA ABREBIAR EL NUMPAY
lista = [1,2,3,4,5,6]

arr = np.array(lista)

print(lista)
print (arr)
print(arr[2])
#SE PUEDE HACER CASI TODO LO MISMO QUE CON LAS LISTAS
print(arr.shape) #SHAPE NOS DEVUELVE LA CANTIDAD DE ELEMENTOS POR DIMENSION

#CREACION DE UNA MATRIZ
lista2 = [[1,2],[3,4],[5,6],[7,8]]
matriz = np.array(lista2)
print(matriz)
print(matriz.shape)
#ACCEDER A ELEMENTOS DESDE LA MATRIZ
print(matriz[3][1])
#ACCEDER PERO DESDE NUMPY
print(matriz[3, 1]) #TABIEN LE PEDO ASIGNAR VALORES ASI

#FUNCIIONALIDADES DE NUMPY
#CREAR ARREGLO DE SOLO 0s
arr_zeros = np.zeros((5,3))
print(arr_zeros)
#ARREGLOS DE UNA SOLA DIMENSION
arr_zeros = np.zeros(5,)
print(arr_zeros)

#CREAR ARREGLOS CON SOLO 1s
arr_ones = np.ones((5,3))
print(arr_ones)
#CON OTROS NUMEROS SERIA 
print (3*arr_ones)

#APLICAR OPERADOR DE SUBSCRIPTS
 #COPIAR Y PEGAR DE LA PRESENTACION (qUE A FECHA DE HOY NO APARECE)

#OBLIGAR A USAR TPO DE DATO ESPECIFICO
arr_matrix = np.array(lista2, dtype=np.int64)
print (arr_matrix)

#OPERACIONES CON Y ENTRE ARREGLOS

#SUMAR DOS MATRICES
l1 = [[1,2,5], [3,4,6]]
l2 = [[5,6,-1], [7,8,-6]]
suma = []
for i in range(len(l1)):
    suma.append([])
    for j in range(len(l2[i])): #NI VERGGAS NO ENTENDI JAJAJA
        suma[i].append(l1[i][j] + l2[i][j])
print(suma)
#AHORA CON NUMPY
arr1 = np.array(l1)
arr2 = np.array(l2)
print (arr1 + arr2)
#MULTIPLICACION VALOR POR VALOR
print (arr1 * arr2)
#CALCULAR RAIZ DE ELEMENTOS
print(np.sqrt(arr1))

#MULTIPLICACION MATRICIAL DE MATRICES
# print(np.matmul(arr1, arr2)) #NO CORRE POR LAS DIMENSIONES

#FUNCION LINSPACE
arr3 = np.linspace(2, 3, num=10, endpoint=False, retstep=True) #nuum RECIBE LA CANTIDAD DE NUMEROS QUE QUIERO RECIBIR
#ENDPOINT FALSE EXCLUYE EL ULTIMO NUMERO DEL RANGO QUE ENVIE
#RETSTEP NOS ENVIA UNA TUPLA Y ME DICE EL PASO ENTRE CADA NUMERO
print (arr3) #EN ESTE CASO CREA 50 NUMEROS ENTRE 2 Y 3 Y ESTAN UNIFORMEMENTE DISTRIBUIDOS

