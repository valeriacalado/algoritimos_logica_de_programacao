salario_atual = float(input("Digite o salário da pessoa: "))

if salario_atual <= 1000:
    novo_salario = salario_atual + salario_atual * 0.2
    aumento = novo_salario - salario_atual
    print(f'Novo salário = R$ {novo_salario:.2f}')
    print(f'Aumento = R$ {aumento:.2f}')
    print("Porcentagem = 20 %")

elif 1000 < salario_atual <= 3000:
    novo_salario = salario_atual + salario_atual * 0.15
    aumento = novo_salario - salario_atual
    print(f'Novo salário = R$ {novo_salario:.2f}')
    print(f'Aumento = R$ {aumento:.2f}')
    print("Porcentagem = 15 %")

elif 3000 < salario_atual <= 8000:
    novo_salario = salario_atual + salario_atual * 0.1
    aumento = novo_salario - salario_atual
    print(f'Novo salário = R$ {novo_salario:.2f}')
    print(f'Aumento = R$ {aumento:.2f}')
    print("Porcentagem = 10 %")

elif salario_atual > 8000:
    novo_salario = salario_atual + salario_atual * 0.05
    aumento = novo_salario - salario_atual
    print(f'Novo salário = R$ {novo_salario:.2f}')
    print(f'Aumento = R$ {aumento:.2f}')
    print("Porcentagem = 5 %")