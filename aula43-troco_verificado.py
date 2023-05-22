preco_unitario = float(input("Preço unitário do produto: "))
quantidade_comprada = float(input("Quantidade comprada: "))
dinheiro_recebido = float(input("Dinheiro recebido: "))

troco = dinheiro_recebido - (preco_unitario * quantidade_comprada)

if troco < 0:
    dinheiro_faltante = troco * -1
    print(f'DINHEIRO INSUFICIENTE. FALTAM {dinheiro_faltante:.2f} REAIS')