"""
Crie um programa que leia os catetos de um triângulo retângulo e retorne o valor da hipotenusa
"""

from math import hypot

cateto1 = float(input("Digite o valor do cateto opposto: "))
cateto2 = float(input("Digite o valor do cateto adjacente: "))

hipotenusa = hypot(cateto1, cateto2)

print(f"O valor da Hipotenusa é: {hipotenusa}")

"""
from math import sqrt

cateto1 = float(input("Digite o valor do cateto oposto: "))
cateto2 = float(input("Digite o valor do cateto adjacente: "))

hipotenusa = sqrt(cateto1 ** 2 + cateto2 ** 2)
# Calcula a hipotenusa usando o Teorema de Pitágoras

print(f"O valor da Hipotenusa é: {hipotenusa}")


(cateto1 ** 2 + cateto2 ** 2) ** (1/2)
"""