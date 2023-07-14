"""
    Faça um programa que leia algo pelo teclado e mostre na tela o seu
    tipo primitivo e todas as informações possíveis sobre ele.
"""
valor = input('Digite um valor: ')

print(f'O tipo primitivo desse valor é , \033[4;34m{type(valor)}\033[m')
print(f'Só tem espaço? \033[4;34m{valor.isspace()}\033[m')
print(f'É um número? \033[4;34m{valor.isnumeric()}\033[m')
print(f'É alfabético \033[4;34m{valor.isalpha()}\033[m')
print(f'É alfanumérico \033[4;34m{valor.isalnum()}\033[m')
print(f'Está tudo em maísculo? \033[4;34m{valor.isupper()}\033[m')
print(f'Está tudo em minúsculo? \033[4;34m{valor.islower()}\033[m')
print(f'Está capitalizada? \033[4;34m{valor.istitle()}\033[m')
