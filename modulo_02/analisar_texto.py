"""
Crie um programa que leia um texto e retorne:
1 - O texto com todas as letras maiúsculas
2 - O texto com todas as letras minúsculas
3 - Quantas letras ao todo sem considerar espaços
4 - Quantas letras tem a primeira palavra
"""

texto = str(input("Digite qualquer coisa: "))

print("texto em maiúscula")
print(texto.upper())
print()

print("Texto em minúscula")
print(texto.lower())
print()

print("Contando as letras sem os espaços vazio")
print(len(texto.replace(" ", "")))
print()

print("Contando quantas letras tem a primeira palavra")
primeira_palavra = texto.split()
print(len(primeira_palavra[0]))

"""
Alguns que acho importante estudar:

.strip()
Remove espaços em branco do início e do fim da string. É ótimo para limpar entradas do usuário:
frase_suja = "   Olá, mundo!   "
frase_limpa = frase_suja.strip()
print(f"'{frase_limpa}'") # Saída: 'Olá, mundo!'

.title()
Converte a primeira letra de cada palavra para maiúscula.
nome = "maria da silva"
nome_formatado = nome.title()
print(nome_formatado) # Saída: Maria Da Silva

.join(lista)
Junta os elementos de uma lista de strings em uma única string, 
usando o caractere da string como separador. É o "oposto" do .split().
palavras = ["Python", "é", "muito", "legal"]
frase = " ".join(palavras)
print(frase) # Saída: Python é muito legal

.isdigit()
Verifica se a string contém apenas dígitos (números).
codigo = "12345"
cep = "04578-000"
print(codigo.isdigit()) # Retorna True
print(cep.isdigit())    # Retorna False (por causa do traço)

.isalpha()
Verifica se a string contém apenas letras (sem números ou espaços).
texto1 = "Python"
texto2 = "Python 3"
print(texto1.isalpha()) # Retorna True
print(texto2.isalpha()) # Retorna False

.startswith('prefixo')
Verifica se a string começa com um determinado texto.
frase = "Python é incrível"
print(frase.startswith("Python"))     # Retorna True
print(frase.startswith("incrível"))   # Retorna False

.endswith('sufixo')
Verifica se a string termina com um determinado texto.
frase = "Python é incrível"
print(frase.endswith("Python"))     # Retorna False
print(frase.endswith("incrível"))   # Retorna True
"""