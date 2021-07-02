#LIBRERIA PARA MANIPULAR DATOS
#GUARDA LOS DATOS EN COLUMNAS PARA CREAR DATAFRRAMES

dictc = {"country": ["Brazil", "Russia", "India",
"China", "South Africa", "Colombia"],
"capital": ["Brasilia", "Moscow", "New Dehli",
"Beijing", "Pretoria", "Bogot ́a"],
"area": [8.516, 17.10, 3.286, 9.597, 1.221, 1.142],
"population": [200.4, 143.5, 1252, 1357, 52.98, 49.65] }

import pandas as pd
brics = pd.DataFrame(dictc) #IMPORTAMOS EL DICCIONARIO COMO UN DATAFRAME
print(brics)
print(brics["area"].mean()) #IMPRIMER EL PROMEDIO DEL DATO DE LOS VALORES DE LA COLUMNA
print(dictc)
print(brics.info()) #INFORMACION DE DATOS
print(brics.describe()) #SACA ALGUNAS ESTADISTICAS DE DATOS NUMERICOS

#BUSCAR UNFORMACION MAS ESPECIFICA
print(brics["country"] == "Colombia")

#LEER INFORMACION DE UN CSV
ventasdf = pd.read_csv("Manejo de Archivos/files/SalesJan2009.csv")
print(ventasdf.head(5)) #IMPRIME LOS PRIMEROS N DATOS

from collections import Counter
#ME SIRVE POR EJEMPLO PARA HACER TABLAS DE FRECUENCIAS
p_counter = Counter(ventasdf["Country"])
print(p_counter)

print(p_counter.most_common(3)) #MUESTRA LA CANTIDAD DE REPETICIONES DE CADA UNO

#GRAFICAR DATOS CON PANDAS

import datetime #CONVIERTE LA COLUMNA DE FECHAS PORQUE ORIGINALMENTE SON STRINGS
import matplotlib.pyplot as plt

#Reporte por fecha
ventasdf["Transaction_date"]=pd.to_datetime(ventasdf["Transaction_date"])
A = (ventasdf["Transaction_date"]
.dt.floor("d")
.value_counts()
.rename_axis("date")
.reset_index(name="num ventas"))
G=A.plot(x="date",y="num ventas",color="green",title="Ventas por fecha")
plt.show()