#!/usr/bin/env python3

"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR ou
    LANG=it_IT python3 hello.py

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__author__  = "Alexandre Souza"
__license__ = "Unlicense"

import os # biblioteca externa

current_language = os.getenv("LANG", "en_US")[:5] # en_US variavel padrao
# variavel no padrao snake case

# Orden O(1)

msg ={
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Mond!",
}

print(msg[current_language])



# # Ordem O(n)
# msg = "Hello, World"
# 
# if current_language == "pt_BR":
#     msg = "Olá, Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "es_SP":
#     msg = "Hola, Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde!"

# print(msg) # comentario