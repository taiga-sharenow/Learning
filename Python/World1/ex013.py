"""
    Faça um algoritmo que leia o salário de um funcionário e mostre seu 
    novo salário, com 15% de aumento
"""
porcent = 15
salario = float(input('Digite o valor do seu salário: '))

porcent_salario = salario * porcent / 100
novo_salario = salario + porcent_salario

print(f'O valor do salario com o aumento de \033[4;31m{porcent}%\033[m, o valor do aumento é \033[4;31mR${porcent_salario}\033[m, acrescentado é: \033[4;31mR${novo_salario}\033[m')