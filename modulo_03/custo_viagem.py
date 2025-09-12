"""
Exercício: Cálculo do Custo da Viagem
Crie um programa que pergunte a distância de uma viagem em quilômetros.
Se a viagem for até 200 km, o programa deve calcular o valor usando a tarifa normal. 
Se a viagem for acima de 200 km, deve aplicar um preço promocional por km.
Até 200 km → R$ 1,10 por km
Acima de 200 km → R$ 0,95 por km (promoção)
Exiba o valor total da viagem ao final.
"""

distancia = float(input("Digite a distância da viagem: "))

# testanto if ternário
preco = distancia * 1.10 if distancia <= 200 else distancia * 0.95
print(f"O valor da viagem é R$ {preco:.2f}")