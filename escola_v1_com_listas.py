#!/usr/bin/env python3

"""Exibe relatorio de criancas por atividade

Imprimir a lista de criancas agrupadas por sala que frequentan cada uma das atividades.
"""
__version__ = "0.1.0"
__author__  = "Alexandre Souza"
__license__ = "Unlicense"

### Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joana", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik","Maia","Joana","Carlos","Antonio"]
aula_musica = ["Erik","Carlos","Maria"]
aula_danca = ["Gustavo","Sofia","Joana","Antonio"]

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
    ]

### Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:
    print("-" * 50)
    print(f"Alunos das atividade {nome_atividade}:\n")
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print(f"{nome_atividade} sala 1 ", atividade_sala1)
    print(f"{nome_atividade} sala 2 ", atividade_sala2)
print()
print("#" * 50)