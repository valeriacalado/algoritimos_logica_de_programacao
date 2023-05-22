distancia1 = float(input("Digite a primeira distância: "))
distancia2 = float(input("Digite a segunda distância: "))
distancia3 = float(input("Digite a terceira distância: "))

maior = sorted([distancia1, distancia2, distancia3])

print(f'MAIOR DISTÂNCIA = {maior[-1]}')
