"""
    Escreva um programa que conversa uma temperatura
    digitada em °C e converta para °F
"""
temp_cel = float(input('Coloque a temperatura em Celsius: '))

temp_fahr = (temp_cel * 9/5) + 32

print('Celsius (\033[1;33m{}°C\033[m) = Fahrenheit (\033[1;31m{}°F\033[m)'.format(temp_cel, temp_fahr))