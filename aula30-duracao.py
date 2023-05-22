"""
DURACAO
Fazer um programa para ler uma duração de tempo em segundos, daí 
imprimir na tela esta duração no formato horas:minutos:segundos.
"""

import datetime

def convertersegundos(duracao):
    return str(datetime.timedelta(seconds = duracao))

duracao = input("Digite a duração em segundos: ")
duracao = float(duracao)

print(convertersegundos(duracao))

"""
def soma(x,y):
    result = x + y
    return result

a = int(input("Primeiro numero: "))
b = int(input("Segundo número: "))
res = soma(a,b)
print("Soma: ", res)
"""
