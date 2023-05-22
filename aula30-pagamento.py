"""
PAGAMENTO
Fazer um programa para ler o nome de um(a) funcionário(a), o valor 
que ele(a) recebe por hora, e a quantidade de horas trabalhadas por 
ele(a). Ao final, mostrar o valor do pagamento do funcionário com uma 
mensagem explicativa, conforme exemplo.
"""

nome = input("Nome: ")
valor = input("Valor por hora: ")
horas = input("Horas trabalhadas: ")

valor = float(valor)
horas = float(horas)

pagamento = valor * horas

print("O pagamento para", nome, "deve ser", pagamento)