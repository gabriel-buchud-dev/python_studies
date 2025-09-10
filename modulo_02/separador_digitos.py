"""
Escreva um programa que leia um número de 0 até 9999 e retorne os segintes dados:
unidade, dezena, centena e milhar.
"""

numero_str = input("Digite um número de 0 a 9999: ")
numero_int = int(numero_str)

if numero_int > 9999:
    print("Digite um número abaixo de 9999.")
elif numero_int < 0:
    print("Digite um número a partir de 0.")
else:
    numero_str = numero_str.zfill(4)  # garante 4 dígitos
    print(f"{'Posição':15} Número")
    print(f"{'Unidade':15} {numero_str[3]}")
    print(f"{'Dezena':15} {numero_str[2]}")
    print(f"{'Centena':15} {numero_str[1]}")
    print(f"{'Milhar':15} {numero_str[0]}")


"""
Primeiro modo que achei para resolver o exercício:
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f"{'Posição':15} Número")
print(f"{'Unidade':15} {unidade}")
print(f"{'Dezena':15} {dezena}")
print(f"{'Centena':15} {centena}")
print(f"{'Milhar':15} {milhar}")

Não utilizei essa resolução pois o intuito é aprender mais sobre módulos e manipulação.
"""