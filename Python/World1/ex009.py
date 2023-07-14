"""
    Faça um programa que leia um número inteiro qualquer e mostre na 
    tela a sua tabuada.
"""
valor = int(input('Insira um valor inteiro: '))

for i in range(11):

    result = valor * i

    print(f'\033[1;33m{valor}\033[m * \033[1;35m{i}\033[m = \033[1;32m{result}\033[m')
    
    print('-' * 5)