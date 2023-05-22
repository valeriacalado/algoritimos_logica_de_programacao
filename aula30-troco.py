"""
TROCO
Fazer um programa para calcular o troco no processo de pagamento de 
um produto de uma mercearia. O programa deve ler o preço unitário do 
produto, a quantidade de unidades compradas deste produto, e o valor 
em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). 
Seu programa deve mostrar o valor do troco a ser devolvido ao cliente.
"""

preco = input("Preço unitário do produto: ")
quantidade = input("Quantidade comprada: ")
pagamento = input("Dinheiro recebido: ")

preco = float(preco)
quantidade = float(quantidade)
pagamento = float(pagamento)

troco = pagamento - (preco * quantidade)

print("Troco =", troco)


"""
def calculodotroco(x, y, z):
    resultado = x - (y * z)
    return resultado

preco = input("Preço unitário do produto: ")
quantidade = input("Quantidade comprada: ")
pagamento = input("Dinheiro recebido: ")

preco = float(preco)
quantidade = float(quantidade)
pagamento = float(pagamento)

troco = calculodotroco(pagamento, quantidade, preco)
print(troco)
"""

