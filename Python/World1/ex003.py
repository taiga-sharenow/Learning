"""
    Crie um programa que leia dois números e mostre a soma entre eles.
"""
num1 = int(input('\033[1;35mDigite um número inteiro:\033[m '))
num2 = int(input('\033[1;32mDigite um número inteiro:\033[m '))

result = num1 + num2

print('O resultado da soma entre \033[1;35m{}\033[m e \033[1;32m{}\033[m é \033[1;34m{}\033[m'.format(num1, num2, result))