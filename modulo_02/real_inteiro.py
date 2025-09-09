"""
Crie um programa que leia um número real qualquer pelo teclado e
mostre na tela a sua porção inteira

ex: 6.127 tem a sua parte inteira 6.
"""

from math import trunc # Importa apenas a função trunc da biblioteca math

numero_real = float(input("Digite um número: "))

print(f"O número {numero_real}, tem a sua parte inteira {trunc(numero_real)}")


"""
Outra possível solução é:
print(f"O número {numero_real}, tem a sua parte inteira {int(numero_real)}")
nesse caso não é necessário importar a função math e nem usar o truncate.
"""