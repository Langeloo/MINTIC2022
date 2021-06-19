#Es una estructura de datos que guardan datos de todos los tips, y su tipo de dato es tupla
tupla1 = ("jajaja", 12, 12.1)
tupla2 = (1, 2, 3, 4, 3, 4)
#tupla de tuplas
tupla3 = (tupla1, tupla2)
type(tupla3)
#concatenar tuplas
tupla4 = (tupla1 + tupla2 + tupla3)
print(tupla4)
#OPERADOR REPETIR
tupla5 = (tupla4 * 3)
print(tupla5)
#COMPARACION DE TUPLAS
#ORDEN LEXICOGRAFICO, ES DECIR, EMPEZAAZR DESDE LA IZQUIERDA
print(tupla5 > tupla4)
# HAY QUE TENER CUIDADO QUE LOS PARESDE COMPARACION SEAN DEL MISMO TIPO, DARIA ERROR

#SUBINDICES DE TUPLAS
#Igual que vectores jaja, SI PONGO INDICECS NEGATIVOS CUENTA DE PARA ATRAZ

#INTERCAMBIAR VALORES ENTRE VARIABLES
# a, b = b, a
#... Estudiar xd

#FUNCION MAP
# NO ENTENDI PUTA MADRE
#CREO QUE LE PALICA FUNCIONES A ELEMENTOS, A CADA ELEMENTO DE UNA ESTRUCTURA, ENTONCES SE OBTIENE OTRO ELEMENTO ITERABLE
#CORREO DEL PROFE
# jccastrop@unal.edu.co
