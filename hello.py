#!/usr/bin/env python3

"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR ou
    LANG=it_IT python3 hello.py
    escolha a lingua

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__  = "Alexandre Souza"
__license__ = "Unlicense"

import os # biblioteca externa
import sys

arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Ivalid Option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: Usar repeticao
    if current_language is None: 
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg ={
    "en_US": "Hello, World! 🇺🇸",
    "pt_BR": "Olá, Mundo! 🇧🇷",
    "it_IT": "Ciao, Mondo! 🇮🇹",
    "es_SP": "Hola, Mundo! 🇪🇸",
    "fr_FR": "Bonjour, Mond! 🇫🇷",
}

print(msg[current_language] * int(arguments["count"]))



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