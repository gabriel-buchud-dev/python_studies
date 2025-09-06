print("Calculadora de Aluguel de Carros")

dias = int(input("Quantos dias alugado?: "))
km_percorrido = float(input("Quantos km rodados?: "))

valor_dias = 60 * dias # 60 reais o valor da diária
valor_km = 2.45 * km_percorrido # R$ 2.45 o valor do km
total = valor_dias + valor_km

print(f"\n{'Descrição':20} {'Valor'}")
print("-" * 30)
print(f"{'Dias alugados:':20} R$ {valor_dias:.2f}")
print(f"{'KM percorridos:':20} R$ {valor_km:.2f}")
print(f"{'Total:':20} R$ {total:.2f}")
