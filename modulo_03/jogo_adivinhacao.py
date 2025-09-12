"""
Exercício: Jogo de Adivinhação
Crie um programa que escolha um número de 1 a 5 aleatoriamente e peça para o 
usuário tentar adivinhar qual número foi escolhido, mostrando se ele acertou ou errou.
"""
import time
import random

acerto = [
    "Mandou bem! 😎",
    "Acertou! Nem eu esperava… 😂",
    "Número correto! Tá afiado hoje!",
    "Uhuu! Pegou o número certo!"
]

erro = [
    "Ops, errou! Tenta de novo 😅",
    "Não foi dessa vez… Mas segue tentando!",
    "Quase lá! Quem sabe na próxima? 😉",
    "Nada feito! Tenta outra vez!"
]

random_numero = random.randint(1, 5)

print("\nTente adivinhar em que número irei pensar.\n")

while True:
    print("-=-" * 15)
    numero_usuario = int(input("Escolha um número de 1 a 5: "))
    print("Processando...")
    time.sleep(1.5)
    print("-=-" * 15)
    
    if numero_usuario > 5 or numero_usuario < 1:
        print("O número não está no intervalo de 1 a 5, tente novamente.")
    elif numero_usuario == random_numero:
        print(random.choice(acerto))
        break
    else:
        print(random.choice(erro))
    
