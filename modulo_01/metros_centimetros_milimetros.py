print("Metros > Centímetros > Milímetros")

metros = float(input("Digite a quantidade de metros: "))

print("")
print(f"{metros}m em centímetros é: {metros * 100}cm")
print(f"{metros}m em milímetros é: {metros * 1000}mm")
print("")

print(f"{'Unidade':<15}{'Valor'}")
print(f"{'Centímetros':<15}{metros*100}")
print(f"{'Milímetros':<15}{metros*1000}")

"""
O :<15 dentro da f-string é uma instrução de formatação. Vamos quebrar:
: → indica que vem uma especificação de formatação.
< → significa alinhamento à esquerda (left).
15 → é a largura mínima do campo, ou seja, esse espaço vai ocupar pelo menos 15 caracteres.
"""