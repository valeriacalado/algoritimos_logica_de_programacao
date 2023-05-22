a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

delta = (b ** 2) - (4 * a * c)

if a == 0:
    print("O valor de a deve ser diferente de 0")

elif delta < 0:
    print("A equação não possui raízes reais")

else:
    x1 = (-b + (delta ** 0.5)) / 2 * a
    x2 = (-b - (delta ** 0.5)) / 2 * a

    print(f'X1 = {x1:.4f}\nX2 = {x2:.4f}')