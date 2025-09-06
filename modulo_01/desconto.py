print("Calculadora de Desconto")

valor_produto = float(input("Digite o valor do produto: "))
desconto = int(input("Digite o valor do desconto em %: "))

preco_final = valor_produto - (valor_produto * desconto / 100)

print(f"O valor final com desconto é de: R$ {preco_final:.2f}")
print(f"E o valor economizado foi de: R$ {valor_produto * desconto / 100:.2f}")