with open("files/SalesJan2009.csv", "r") as f:
    flag = True
    conteos = {}
    for line in f:
        if flag:
            flag = False
        else:
            datos = line.split(",")
            country = datos[7]
            if country in conteos:
                conteos[country] += 1
            else:
                conteos[country] = 1
#COMO HACERLO EN UNA SOLA LINEA, APORTE DE UN PANA
# conteos[country] = conteos.get(country, 0) + 1
print(conteos)
#COLAB: https://colab.research.google.com/drive/1D-u-ZmMFs_40-RqpA59s1wAO2HmrQAxX?usp=sharing&authuser=1