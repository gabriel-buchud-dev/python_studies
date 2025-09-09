"""
Um professor deseja sortear um aluno dentre 10 na sala. 
Faça um programa que leia os nomes dos alunos e escolha aleatoriamente um deles.
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

aluno_sorteado = random.choice(alunos)

print(f"O aluno sorteado da vez é: {aluno_sorteado}")


"""
A primeira forma que pensei para resolver esse exercício foi através de índices.
indice = random.randint(0, 9) 
aluno_sorteado = nomes[indice]
print(f"O aluno sorteado da vez é: {aluno_sorteado}")
como a lista vai de 0 até 9, o índice sorteado aponta para o aluno correspondente

outra opção seria fazer:
print(f"O aluno sorteado da vez é: {nomes[random.randint(0, 9)]}")
direto no print.
"""