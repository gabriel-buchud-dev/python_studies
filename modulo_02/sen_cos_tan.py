"""
Crie um programa que leia um ângulo qualquer e mostre na tela 
o valor do seno, cosseno e tangente desse ângulo.
"""

from math import sin, cos, tan, radians

angulo = float(input("Digite o Ângulo: "))

angulo_radianos = radians(angulo) # Converte o ângulo de graus para radianos

print("-" * 25)
print(f"{'Razões':10} {'Valores'}")
print("-" * 25)
print(f"{'Seno':10} {sin(angulo):.5f}")
print(f"{'Cosseno':10} {cos(angulo):.5f}")
print(f"{'Tangente':10} {tan(angulo):.5f}")



"""
sin = cateto_oposto / hipotenusa
cos = cateto_adjacente / hipotenusa
tan = cateto_oposto / cateto_adjacente
"""