"""
Exercício: Radar de Velocidade
Crie um programa que simule um radar de carro. 
O programa deve pedir a velocidade do veículo e verificar se o motorista ultrapassou 80 km/h. 
Para cada km acima do limite, o motorista deve receber uma multa de R$7,00. 
Mostre o valor da multa ou uma mensagem informando que não há infração.
"""
import time
import random

print("\n=== RADAR DE VELOCIDADE ===\n")

print("-+-" * 15)
# Para testar com valores fixos, comente a linha abaixo e descomente a linha do input.
velocidade = random.randint(20, 150); print("Seu carro passou pelo radar...")
# velocidade = int(input("Informe a velocidade do veículo: "))
print("-+-" * 15, "\n") 

if velocidade < 0:
    print("Velocidade inválida.\n")
elif velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"\033[31mAtenção, motorista! Multa na área 🚨\033[m")
    print(f"Velocidade registrada: {velocidade} km/h 📸")
    print("O valor da multa é de R$ 7,00 por km acima do permitido 🚨\n")
    print("Processando...")
    time.sleep(1)
    print(f"\033[31mValor final da multa: R$ {multa:.2f}\033[m\n")
else:
    print(f"Velocidade registrada: {velocidade} km/h 📸")
    print(f"\033[32mParabéns! Você está dentro do limite de velocidade 🚗💨\033[m")
