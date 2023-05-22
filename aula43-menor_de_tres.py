primeiro_valor = int(input("Primeiro valor: "))
segundo_valor = int(input("Segundo valor: "))
terceiro_valor = int(input("Terceiro valor: "))

if primeiro_valor == segundo_valor and segundo_valor == terceiro_valor:
    print(f'MENOR = {primeiro_valor}')

else:
    menor = sorted([primeiro_valor, segundo_valor, terceiro_valor])
    print(f'MENOR = {menor[0]}')