#print("Hello, world")
#characters = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","+","-","*","/","%"]

juan_input = list(input("Datos de Juan: "))
camilo_input = list(input("Datos de Camilo: "))
bag_input = input("Datos de bolsa: ")
#print(juan_input) FUNCIONA CORRECTAMENTE

juan_score = 0
camilo_score = 0
final_score = ""


for x in bag_input:
    if juan_input.__contains__(x):
        juan_score+=1
    if camilo_input.__contains__(x):
        camilo_score+=1
    if juan_score == camilo_score:
        final_score+="T"
    elif juan_score > camilo_score:
        final_score+="J"
    else:
        final_score+="C"
        
print(final_score)