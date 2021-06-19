from os import system


#FUNCIONES

def menu():
    system("cls")
    print("1. Retiros: (1&[Valor del retiro]&[Razon])\n2. Depositos: (2&[#10]&[#20]&[#50]&[Razon])\n3. Consultar retiros: (3&[Mayor o Menor])\n4. Consultar depositos: (4&[Mayor o Menor])\n5. Salir \n10")
    #AQUI EXPLICO COMO INGRESAR LOS VALORES
    program = input("Digite la accion que quiere realizar: ").split("&")
    system("cls")
    if int(program[0]) == 1:
        retreats(program)
    elif int(program[0]) == 2:
        deposits(program)
    elif int(program[0]) == 3 or int(program[0]) == 4:
        consults(program, 3) if int(program[0]) == 3 else consults(program, 4)
    elif int(program[0]) == 5:
        system("exit")
    else:
        print("Opcion incorrecta")
        system("pause")
        menu()


def retreats(program):
    def count_tickets(ticket, money, c_tickets): #Esta es la que defini dentro de otra, la saque pero me daba error, la deje mientras
        module = money % ticket
        c_ticket = money // ticket
        while c_ticket > c_tickets:
            c_ticket -= 1
            module += ticket
        d_return = [c_ticket, module]
        return d_return
    print("RETIROS".center(30, "/"))
    value_retreat = int(input("Digite el valor a retirar: "))
    if value_retreat > money:  # debo definirlo pero igual funciona xd
        print("Saldo insuficiente.")
        system("pause")
        menu()
    elif value_retreat > ((ticket50 * 50) + (ticket20 * 20) + (ticket10 * 10)):
        print("El cajero no tiene el dinero suficiente.")
        system("pause")
        menu()
    else:
        t = count_tickets(50, value_retreat, ticket50)
        print("Retirar: {}\nBilletes de 50: {}".format(value_retreat, t[0]))
        ticket50 -= t[0]
        t = count_tickets(20, t[1], ticket20)
        print("Billetes de 20: {}".format(t[0]))
        ticket20 -= t[0]
        t = count_tickets(10, t[1], ticket10)
        print("Billetes de 10: {}".format(t[0]))
        ticket10 -= t[0]
        temporal_list = [value_retreat, program[2]]
        retreats_list.append(temporal_list)
        system("pause")
        menu()


def deposits(program):
    print("DEPOSITOS".center(30, "/"))
    value_deposit = int(input("Digite el valor del deposito: "))
    print("Digite la cantidad de cada denominacion: ")
    ticket50_d = int(input("Billetes de 50: "))
    ticket20_d = int(input("Billetes de 20: "))
    ticket10_d = int(input("Billetes de 10: "))
    if ((ticket10_d * 10) + (ticket10_d * 10) + (ticket10_d * 10)) == value_deposit:
        ticket10 += ticket10_d
        ticket20 += ticket20_d
        ticket50 += ticket50_d
        temporal_list = [value_deposit, program[4]]
        deposits_list.append(temporal_list)
        print("Dinero depositado.")
        system("pause")
    else:
        print("El valor digitado no corresponde con los billetes.")
        system("pause")
        menu()

def consults(program, value):
    if program[1].lower == "menor":
        if value == 3:
            print("MENOR RETIROS".center(30, "/") + "\n" + str(min(retreats_list)))
        else:
            print("MENOR DEPOSITOS".center(30, "/") + "\n" + str(min(deposits_list)))
    elif program[1].lower == "mayor":
        if value == 3:
            print("MAYOR RETIROS".center(30, "/") + "\n" + str(max(retreats_list)))
        else:
            print("MAYOR DEPOSITOS".center(30, "/") + "\n" + str(max(deposits_list)))
    else:
        return "Valores erroneos"
        


#PROGRAMA CAJERO AUTOMATICO (MAIN)
retreats_list = []
deposits_list = []
system("cls")
print("Digite la cantidad inicial de cada denominacion: ")
ticket50 = int(input("Billetes de 50: "))
ticket20 = int(input("Billetes de 20: "))
ticket10 = int(input("Billetes de 10: "))
money = int(input("Digite la cantidad de dinero del usuario: "))
system("cls")
menu()
