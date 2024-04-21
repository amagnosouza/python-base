#!/usr/bin/env python
"""Imprime a tabuada de 1 a 10.

Tabuada do 1
1
2
3
4
...
____________
Tabuada do 2
2
4
6
...
"""
__version__ = "0.0.1"
__author__ = "Alexandre Souza"

# Definir numeros bases
    # base = [1,2,3,4,5,6,7,8,9,10]

# Outra forma
numeros = list(range(1,11))

# interando

# para cada numero em numeros: 
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("------------")

