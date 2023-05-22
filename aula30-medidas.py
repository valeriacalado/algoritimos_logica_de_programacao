"""
MEDIDAS
Fazer um programa para ler três medidas A, B e C. Em seguida, 
calcular e mostrar (imprimir os dados com quatro casas decimais):
a) a área do quadrado que tem lado A
b) a área do triângulo retângulo que base A e altura B
c) a área do trapézio que tem bases A e B, e altura C
"""

medidaA = input("Digite a medida A: ")
medidaB = input("Digite a medida B: ")
medidaC = input("Digite a medida C: ")

medidaA = float(medidaA)
medidaB = float(medidaB)
medidaC = float(medidaC)

areaquadrado = medidaA ** 2

areatriangulo = (medidaA * medidaB) / 2

areatrapezio = ((medidaA + medidaB) * medidaC) / 2 

print("Área do quadrado =", f'{areaquadrado:.4f}')
print("Área do triângulo =", f'{areatriangulo:.4f}')
print("Área do trapézio =", f'{areatrapezio:.4f}')