escala = input("Você vai digitar a temperatura em qual escala (C/F)? ")

if escala == 'C':
    temp_informada_Celsius = float(input("Digite a temperatura em Celsius: "))
    temp_convert_para_F = temp_informada_Celsius * 1.8 + 32
    print(f'Temperatura equivalente em Fahrenheit: {temp_convert_para_F:.2f}')

if escala == 'F':
    temp_informada_Fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    temp_convert_para_C = (temp_informada_Fahrenheit - 32) / 1.8
    print(f'Temperatura equivalente em Celsius: {temp_convert_para_C:.2f}')