print('Hello, world')
def division(a,b):
    coc = a//b
    res = a%b
    return coc, res

try:
    print(division(5,0)) #ponemos el codigo que creo que me da error
except:
    print('Division entre 0')
else:
    print('Todo salio bien') #si no envia la excepcion, pasa al else
print(division(5,3))
#print(division(5,0))
print(division(15,3))

lista = [10, 20]
try:
    print(lista[2])
except:
    print("Indice Invalido")
else:
    print('Todo bello')
#FILTRAR ERRORES

try:
    print(lista[2])
    print(division(5,0))
except IndexError:
    print("Division en 0")
except ZeroDivisionError:
    print("Error dee sintaxix")
except:
    print("Error inesperado")
else:
    print("Todo correcto")

#PRACTICA
try:
    a = int(input("Digite un numero. \n"))
    print(a*2)
except:
    print("No digito un entero")
finally:
    print("Todo ejecutado")

#BLOQUE FINALLY (EJECUTA UNA PORCION DE CODIGO, HAYA O NO HAYA ERROR LUEGO DEL TRY)
#SIRVE MAS PONERLO DENTRO DE UNA FUNCION XD

#COMO IMPRIMIR UN ERROR
try:
    division(5,0)
except Exception as e: #el error se almacena en e
    print(e) #IMPRIME EL TEXTO DE ADVERTENCIA DEL ERROR
    print(type(e)) #IMPRIME EL TIPO DE ERROR

#LANZAR EXCEPCIONES A VOLUNTAD (CREAR ERROR APROPOSITO)
raise ZeroDivisionError('Esta dividiendo entre 0')

#pass es palabra reservada, solo no hace nada, nada de nada, serviria para rellenar un bloque de codigo