"""
Exercício: Par ou Ímpar
Desenvolva um programa que leia um número inteiro informado pelo usuário e verifique se ele é par ou ímpar. 
Caso o valor digitado seja negativo, o programa deve exibir uma mensagem de número inválido.
"""
import time

numero = int(input("Digite um número inteiro: "))

print("Analisando o número...")
time.sleep(1)
if numero % 2 == 0:
    print(f"{numero} é Par! ✅")
else:
    print(f"{numero} é Ímpar! 🔴")
