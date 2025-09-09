"""
Um professor quer sortear a ordem de apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.
"""

import random

alunos = [
    "João", 
    "Maria", 
    "Carin", 
    "Fernanda",
    "Gabriel", 
    "Manuela", 
    "Maysa", 
    "Carlos", 
    "Ana", 
    "Célia"
    ]

random.shuffle(alunos) # embaralha a lista sem repetir ninguém.

print(alunos)

"""
Primeira tentativa foi com:
ordem_apresentacao = random.choices(alunos, k=10)  # k = número de escolhas
print(ordem_apresentacao)
Porém esse método permite repetição, então alguns alunos apareceram mais de uma vez durante os testes.
"""