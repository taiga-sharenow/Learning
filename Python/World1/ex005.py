"""
    Faça um programa que leia um número inteiro e mostre na tela o seu 
    sucessor e seu antecessor.
"""
num = int(input('\033[7;40mDigite um valor:\033[m '))

sucess = num + 1
antecess = num - 1

print('O sucessor do número \033[1;47m{}\033[m é \033[1;33m{}\033[m'.format(num, sucess))
print('O antecessor do número \033[1;47m{}\033[m é \033[1;33m{}\033[m'.format(num, antecess))