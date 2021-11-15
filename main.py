from src.funcs.hopfield import searchPattern, learn
from src.funcs.transforms import transformVectors
import numpy as np

patron = transformVectors(["src/img/a.png","src/img/b.png"])
patron2 = patron[0]
print("patron2")
print(patron2)
if patron2[0] == 1:
    patron2[0] = -1
else:
    patron2[0] = 1
encontrau = searchPattern(patron2, learn(5,5,patron))
print("encontrau")
print(encontrau)