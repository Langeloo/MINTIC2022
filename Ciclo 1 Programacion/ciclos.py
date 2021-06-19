#ESTRUCTURA WHILE
'''
i = 0
while (i <= 6):
   print(i)
   i += 1
'''
# sep = ", " sirve para indicarle al print como quiero que mesepare variables, de ultimas (?)

#ENCONTRAR EL VALOR POSITIVO MAS PEQUEÑO QUUE PUEDE REPRESENTAR PYTHON
'''
n = 1.0
count = 1
while n > 0:
    n /= 2.0
    count += 1
    print (count, n, sep = " :  ")
'''
#DO - WHILE
# tambien con while: True:  Y luego if<condicion>: break
a = 5
while True:
    print('Esto es un do-while')
    a -= 1
    if a < 3:
        break
#EJEMPLO DE USO DE DO-WHILE
#ACABAR UN CICLO ANTICIPADAMENTE con break xd, lo sabia :v, parece que es una mala practica
