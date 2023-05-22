numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

numeros = sorted({numero1, numero2})

if numeros[-1] % numeros[-2] == 0:
    print("São múltiplos")

else:
    print("Não são múltiplos")