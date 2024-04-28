#!/usr/bin/env python3
"""Cadastro de Produto"""
__version__ = "0.1.0"
__author__  = "Alexandre Souza"
__license__ = "Unlicense"

import pprint

produto = {
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,
}

cliente = {
    "nome": "Alexandre"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

#pprint.pprint(compra)

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
)