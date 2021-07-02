#NOS PERMITE GRAFICAR PUNTOS XY
import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4], [1,2,3,4]) #RECIBE PAREMETROS EN X Y Y, DEBEN TENER LA MISMA CANTIDAD DE VALORES
#plt.show() MUESTRA LA GRAFICA


x = np.linspace(0, 2, 50)
#print(x)
# A ́un con el OO-style, usamos ".pyplot.figure" para crear la figura.
fig, ax = plt.subplots() # Crea la figura y los ejes.
ax.plot(x, x, label="linear") # Dibuja algunos datos en los ejes.
ax.plot(x, x**2, label="quadratic") # Dibuja mas datos en los ejes.
ax.plot(x, x**3, label="cubic") # ... y algunos m ́as.
ax.set_xlabel("x label") # Agrega un x-label a los ejes.
ax.set_ylabel("y label") # Agrega un y-label a los ejes.
ax.set_title("Simple Plot") # Agrega t ́ıtulo a los ejes.
ax.legend() # Agrega una leyenda.

#/////////////////////////////////////////////////////////////
names = ["group_a", "group_b", "group_c"]
values = [3.4, 50.3, 23]
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle("Categorical Plotting")
plt.show()
#TIDAS LAS LIBRERIAS TIENEN MUCHAS COSAS, TOCA REVISAR LA DOCUMENTACION

