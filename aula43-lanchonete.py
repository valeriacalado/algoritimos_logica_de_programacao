codigo = input("Código do produto comprado: ")
quantidade = int(input("Quantidade comprada: "))

if codigo == '1':
    valor_1 = 5 * quantidade
    print(f'Valor a pagar: R$ {valor_1:.2f}')

elif codigo == '2':
    valor_2 = 3.5 * quantidade
    print(f'Valor a pagar: R$ {valor_2:.2f}')

elif codigo == '3':
    valor_3 = 4.8 * quantidade
    print(f'Valor a pagar: R$ {valor_3:.2f}')

elif codigo == '4':
    valor_4 = 8.9 * quantidade
    print(f'Valor a pagar: R$ {valor_4:.2f}')
    
elif codigo == '5':
    valor_5 = 7.32 * quantidade
    print(f'Valor a pagar: R$ {valor_5:.2f}')    

