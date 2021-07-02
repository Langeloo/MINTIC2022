#FUNCIONES Y MODULOS
#CREAR Y UTILIZAR MODULOS DESDE 0

#FUNCIONES CON ARGUMENTOS POR DEFECTO
def potencia(a, b = 2): #SI NO ENVIO EL SEGUNDO PARAMETRO, 2 SERA EL VALOR POR DEFECTO
    return a**b

print(potencia(5))
print(potencia(5, 3)) #EN LA DECLARACION, EL VALOR POR DEFECTO DEBE IR AL FINAL A, B = ...

#FUNCIONES CON NUMERO DE ARGUMENTOS VARIABLES
def suma(n, *var1): #EL ASTERISCO INDICA QUE LA FUNCION RECIBIRA N ARGUMENTOS, LOS GUARDARA EN UNA TUPLA
    suma = 0
    for i in var1:
        suma +=i
    return suma * n #VA A TOMAR EL PRIMER VALOR COMO N
res = suma(10,20,30,-13)
print(res)

def imprimir(**elementos): #**SIGNIFICA QUE VA A RECIBIR UN DICCIONARIO
    for k in elementos:
        print(k, " -> ", elementos[k])
imprimir(nombre="Juan", apellido = "Castro", edad = "21")

#PASO DE PARAMETROS
def ordenar(lista):
    lista.sort()
l1 = [5,2,3,8,3,9]
print(l1)
ordenar(l1)
print(l1)

#ALCANCE DE VARIABLES
#DENTRO DE UNA FUNCION PUEDO HACER gobal variable PARA QUE VARIABLE SEA GLOBAL
#SI EN OTRA FUNCION QUIERO USAR VARIABLE TENGO QUE ESCRIBIR GLOBAL TAMBIEN

#MODULOS DE PYTHON

