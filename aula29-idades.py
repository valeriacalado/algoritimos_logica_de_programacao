"""
Fazer um programa para ler o nome e idade de duas pessoas. Ao final,
mostrar uma mensagem com os nomes e a idade média entre essas pessoas,
com uma casa decimal.
"""

print("Dados da primeira pessoa")
nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = input("Digite a idade da primeira pessoa: ")



print("Dados da segunda pessoa")
nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = input("Digite a idade da segunda pessoa: ")

idade1 = float(idade1)
idade2 = float(idade2)

media = (idade1 + idade2) / 2

print("A idade média de", nome1, "e", nome2, "é de", media)
    