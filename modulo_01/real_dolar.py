print("Conversor de Moeda")

print("-" * 50)

real = float(input("Quantos Reais você possui? R$ "))
dolar = real / 5.47 # Cotação do dólar hoje é de 5.47 - 02/09/2025

print("-" * 50)

if dolar < 0.01:
    print("Seu valor é menor que 1 centavo de dólar. Não é possível converter.")
else:
    print(f"Você consegue comprar US${dolar:.2f} dólares.")
