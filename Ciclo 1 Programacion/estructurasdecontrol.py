# IF

# VALOR ABSOLUTO


def absolute_value(number):
    if number < 0:
        return -number
    else: 
        return number
#  number = float(input("Digite un numero: "))
#  print("El valor absoluto es: " + str(absolute_value(number)))


def max_value(number1, number2):
    if number1 > number2:
        return number1
    else: 
        return number2

#OPERADOR TERNARIO

def max_value(number1, number2):
    #pr alguna razon el return solo se debe usar la primeravez o solo asigno una vez
    return number1 if number1 > number2 else  number2

#  print("El mayor es: " + str(max_value(30, 16)))

def alone_if(number):
    if number > -1:
        print("+"+str(number))
        
    print(number)
#  print("jkldsf {} sdfs".format(12))

#OPERADOR LOGICO CONDICIONAL

def conditional(p, q):
  #  if p == True and q == False:
    if p and not q:
        return False
    else:
        return True