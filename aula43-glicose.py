glicose = float(input("Digite a medida da glicose: "))

if glicose < 100:
    print("Classificação: normal")
elif 100 < glicose <= 140:
    print("Classificação: elevado")
else:
    print("Classificação: diabetes")