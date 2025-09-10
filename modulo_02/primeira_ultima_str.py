"""
Escreva um programa que leia uma frase e mostre:
1 - Se tem a letra A e quantas vezes ela aparece na tela
2 - em que posição ela aparece a primeira vez
3 - em que posição ela aparece a última vez
"""

frase = str(input("Digite uma frase: ")).upper().strip()
letra = str(input("Escolha uma letra para ser contabilizada: ")).upper()

print(f"A letra {letra} aparece {frase.count(letra)} vezes na frase.")

print(f"A primeira letra {letra} foi encontrada na posição {frase.find(letra) + 1}")

print(f"A última letra {letra} foi encontrada na posição {frase.rfind(letra) + 1}")