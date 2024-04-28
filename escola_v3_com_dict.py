#!/usr/bin/env python3

"""Exibe relatorio de criancas por atividade

Imprimir a lista de criancas agrupadas por sala que frequentan cada uma das atividades.

#####[DESAFIO]#####
"""
__version__ = "0.1.0"
__author__  = "Alexandre Souza"
__license__ = "Unlicense"

# Dados
alunos = {
    "Erick": {"sala": "sala1"},
    "Maia": {"sala": "sala1"},
    "Gustavo": {"sala": "sala1"},
    "Manuel": {"sala": "sala1"},
    "Sofia": {"sala": "sala1"},
    "Joana": {"sala": "sala1"},
    "Joao": {"sala": "sala2"},
    "Antonio": {"sala": "sala2"},
    "Carlos": {"sala": "sala2"},
    "Maria": {"sala": "sala2"},
    "Isolda": {"sala": "sala2"},
}

aula_ingles = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erick", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = {
    "Inglês": aula_ingles,
    "Música": aula_musica,
    "Dança": aula_danca,
}

# Cria um dicionario para armazenar os alunos de cada sala existente
alunos_por_sala = {"sala1": [], "sala2": []}

# Carrega os alunos de cada sala
for aluno, info in alunos.items():
    alunos_por_sala[info["sala"]].append(aluno)

# Lista alunos em cada atividade por sala
for nome_atividade, atividade in atividades.items():
    print("-" * 50) # pastelaria
    print(f"Alunos da atividade {nome_atividade}:\n")
    
    # Lista de alunos por atividade
    alunos_sala1 = [aluno for aluno in atividade if aluno in alunos_por_sala["sala1"]]
    alunos_sala2 = [aluno for aluno in atividade if aluno in alunos_por_sala["sala2"]]

    print(f"{nome_atividade} sala 1 ", alunos_sala1)
    print(f"{nome_atividade} sala 2 ", alunos_sala2)

print("#" * 50)  # # pastelaria