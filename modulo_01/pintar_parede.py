print("Calculadora de Tinta")

altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))

area_parede = altura * largura
tinta = area_parede / 2 # 1 litro cobre 2m²

print(f"A parede tem {area_parede:.2f}m² e precisará de {tinta:.2f} litros de tinta.")
