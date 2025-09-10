"""
Crie um programa que leia um nome completo e:
1 - Retorne o primeiro nome 
2 - Retorne o último nome
"""

nome = str(input("Digite seu nome completo: ")).strip()
nome_lista = nome.split()

print(f"Seu primeiro nome é: {nome_lista[0]}")
print(f"Seu último nome é : {nome_lista[len(nome_lista) - 1]}")

