#!/usr/bin/env python
"""Imprime a tabuada de 1 a 10.

===Tabuada do 1===
1 x 1 = 1
2 x 1 = 2
3 x 1 = 3
4 x 1 = 4
...
################
"""
__version__ = "0.1.0"
__author__ = "Alexandre Souza"

# Definir numeros bases
    # base = [1,2,3,4,5,6,7,8,9,10]

# Outra forma
numeros = list(range(1,11))

# interando

# para cada numero em numeros: 
for n1 in numeros:
    print(f"=== Tabuada do {n1} ===")
    for n2 in numeros:
        resultado = n1 * n2
        valores = "{:2} x {:2} = {:3}".format(n1, n2, resultado)
        print(valores)
    print("#"*20)
    print()