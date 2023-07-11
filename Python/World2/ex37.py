"""
    Escreva um
    programa que leia um
    número inteiro
    qualquer e peça para o 
    usuário escolher qual
    será a base de
    conversão
    
    -1 para binário
    -2 para octal
    -3 para hexadecimal
"""

val_user = int(input('Digite um número inteiro'))

print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')

option_user = input('Digite: ')

if option_user == '1' :
    result = bin(val_user)
elif option_user == '2' :
    result = oct(val_user)
elif option_user == '3' :
    result = hex(val_user)
else :
    print('Valor Inválido')
    
print(f'O resultado da conversão é {result}')
