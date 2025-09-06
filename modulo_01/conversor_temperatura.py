print("Conversor de Temperatura")

celcius = float(input("Digite a temperauta em Celcius: "))

Fahrenheit = celcius * 1.8 + 32
kelvin = celcius + 273.15

print(f"\n{'Escala':15} {'temperatura'}")
print("-" * 30)
print(f"{'Celcius':15} {celcius:.2f}°")
print(f"{'Fahrenheit':15} {Fahrenheit:.2f}°")
print(f"{'Kelvin':15} {kelvin:.2f}°")