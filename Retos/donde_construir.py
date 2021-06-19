def zone_edifices(third_edifice):
    if third_edifice > 50:
        return "cuatro"
    elif third_edifice > 30:
        return "tres"
    elif third_edifice > 20:
        return "dos"
    else:
        return "uno"

first_edifice = abs(int(input("Altura del primer edificio: ")))
second_edifice = int((first_edifice * 2) + 4)
third_edifice = int((first_edifice + second_edifice)/5)

# RESULTS
print(str(first_edifice) + " " + str(second_edifice) + " " + str(third_edifice))
print(zone_edifices(third_edifice))