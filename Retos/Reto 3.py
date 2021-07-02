bag_input = input("Datos de bolsa: ") + " b"
bag_input = bag_input.split(" ")

len_string = bag_input.__len__()
str_count = 1
caracters_data = ""
numbers_data = ""
data = []


for i in range(len_string - 1):
    caracter = bag_input[i]
    
    if i == len_string - 2 and caracter != bag_input[len_string - 1]:
            data.append([bag_input[i], str_count])
            data.append([bag_input[len_string - 1], 1 ]) 
    elif i == len_string - 2:
            data.append([bag_input[i], str_count + 1])
    elif caracter == bag_input[i + 1]:
        str_count += 1
    else:
        data.append([bag_input[i], str_count])
        str_count = 1

for i in range(data.__len__() - 1):
    #print(data[i][0])
    caracters_data = caracters_data + data[i][0] + " "
    numbers_data = numbers_data + str(data[i][1]) + " "

#caracters_data = caracters_data.split(" ")
#numbers_data = numbers_data.split(" ")
print(caracters_data[:-1])
print(numbers_data[:-1])

#LO DE LA SALIDA SE PUEDE SOLUCIONAR CON UN ELEMENTO ITERABLE
