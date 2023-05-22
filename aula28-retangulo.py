"""
Programa para ler as medidas da base e altura de um retângulo.
Mostrar a área total, perímetro e diagonal, com quatro casas decimais.
"""

base = input("Digite a base do retângulo: ")
altura = input("Digite a altura do retângulo: ")

base = float(base)
altura = float(altura)

area = base * altura

perimetro = (base * 2) + (altura *2)

raiz = (base ** 2) + (altura ** 2)
diagonal = raiz ** 0.5

print("A área do retângulo é:", f'{area:.4f}')
print("O perímetro do retângulo é:", f'{perimetro:.4f}')
print("A diagonal do retângulo é:", f'{diagonal:.4f}')
