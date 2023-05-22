"""
Fazer um programa para ler as medidas da largura e comprimento de um
terreno retangular com uma casa decimal, bem como o valor do metro
quadrado do terreno com duas casas decimais. Em seguida, o programa
deve mostrar o valor da área do terreno, bem como o valor do preço
do terreno, ambos com duas casas decimais.
"""

largura = input("Digite a largura do terreno: ")
comprimento = input("Digite o comprimento do terreno: ")
valormetroquadrado = input("Digite o valor do metro quadrado do terreno: ")
areadoterreno = float(largura) * float(comprimento)

largura = float(largura)
comprimento = float(comprimento)
valormetroquadrado = float(valormetroquadrado)

valordoterreno = areadoterreno * valormetroquadrado


print("A área do terreno é:", f'{areadoterreno:.2f}')
print("O preço do terreno é:", f'{valordoterreno:.2f}')



"""


"""