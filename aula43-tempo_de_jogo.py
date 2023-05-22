hora_inicial = int(input("Hora inicial: "))
hora_final = int(input("Hora final: "))

if hora_inicial > hora_final:
    duracao = (24 - hora_inicial) + hora_final
    print(f'O JOGO DUROU {int(duracao)} HORAS')

elif hora_final == hora_inicial:
    print("O JOGO DUROU 24 HORAS")

else:
    duracao = hora_final - hora_inicial
    print(f'O JOGO DUROU {int(duracao)} HORAS')