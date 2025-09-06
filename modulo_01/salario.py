print("Calculadora de Reajuste de Salário")

salario_inicial = float(input("Digite seu salário atual: "))
valor_reajuste = int(input("Digite o valor do reajuste em %: "))

adicional = salario_inicial * valor_reajuste / 100
novo_salario = salario_inicial + adicional

print(f"O seu novo salário é R$ {novo_salario:.2f} e o valor do reajuste foi de R$ {adicional:.2f}")