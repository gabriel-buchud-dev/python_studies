
print("Média do Aluno")

nota_01 = float(input("Digite a 1° nota do aluno: "))
nota_02 = float(input("Digite a 2° nota do aluno: "))
nota_03 = float(input("Digite a 3° nota do aluno: "))

media = (nota_01 + nota_02 + nota_03) / 3

print(f"A média do aluno foi: {media:.1f}")

if media >= 6:
    print("Aluno Aprovado!")
else:
    print("Reprovado!")