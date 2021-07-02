#CREAR MODULOS
import aritmetica as art #AQUI IMPORTO EL OTRO NDE ESTAN MIS FUNCIONES (AL MISMO NIVEL)
print('suma entre 3 y 7 = ', art.sum1(3, 7))

#VER QUE FUNCIONES TIENE MI MODULO
print(dir(art))

#LOCALIZACION DE MODULOS EN PYTHON
#ESTAN EN PYTHONPATH
import sys
for p in sys.path:
    print(p)

#PAQETES EN PYTHON
#SON CONJUNTOS DE MODULOS QUE LOS ORGANIZO EN UN PAQUETE
from Comprimir import aRar as ar
ar.crear_rar("MiArchivo")
from Comprimir.aTar import crear_Tar

crear_Tar("Vuammooosss!!")