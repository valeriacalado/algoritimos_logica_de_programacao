nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota: "))

notafinal = nota1 + nota2

print(f'NOTA FINAL = {notafinal}')
if notafinal < 60:
    print("REPROVADO")