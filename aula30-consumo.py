"""
CONSUMO
Fazer um programa para ler a distância total (em km) percorrida por
um carro, bem como o total de combustível gasto por este carro ao 
percorrer tal distância. Seu programa deve mostrar o consumo médio 
do carro, com três casas decimais.
"""

distancia = input("Distância percorrida: ")
combustivel = input("Combustível gasto: ")

distancia = float(distancia)
combustivel = float(combustivel)

consumo = distancia / combustivel

print("Consumo médio =", f'{consumo:.3f}')