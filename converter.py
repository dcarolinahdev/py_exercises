# -*- coding: utf-8 -*-
pesos_col = float(input("¿cuántos pesos colombianos tienes? : "))
val_dolar = 3875

dolares = round(pesos_col / val_dolar, 2)
print("Tienes $ "+ str(dolares) + " dólares")