from src.funcs.hopfield import searchPattern, learn
from src.funcs.transforms import transformVectors, transformVector
import numpy as np

#Patrones de entrenamiento
patrones = transformVectors(["src/img/cuatro.png","src/img/cinco.png"])


print("Patrones de entrenamiento:")
print(patrones,"\n")

#Mostramos la matriz general de pesos
matriz_general_de_pesos = learn(5,5,patrones)
print("Matriz general de pesos:")
print(matriz_general_de_pesos,"\n")


#Modificamos un valor del vector 
patron_defectuoso = patrones[0]
if patron_defectuoso[0] == -1:
    patron_defectuoso[0] = 1

print("Patron cambiado:",patron_defectuoso,"\n")


encontrau = searchPattern(patron_defectuoso,matriz_general_de_pesos)
print("Matriz encontrau:", encontrau, "\n")


#Modificamos todo el vector
patron_defectuoso2 = patrones[1]
for i in range(patron_defectuoso2.shape[0]):
    if patron_defectuoso2[i] == -1:
        patron_defectuoso2[i] = 1
        
print("Otro patron defectuoso:", patron_defectuoso2,"\n")

encontrau2 = searchPattern(patron_defectuoso2,matriz_general_de_pesos)
print("Matriz encontrau2:",encontrau2, "\n")
