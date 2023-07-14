"""
    Crie um programa que leia quanto dinheiro uma pessoa tem na 
    carteira e mostre quantos dólares ela pode comprar.
    
    Considere US$1.00 = R$3.37
"""
dolar = 1.00
valor = float(input('Digite a quantidade de dinheiro atualmente: '))

convert_dolar = (valor * dolar) / 3.37

print('A quantidade de \033[4;34mR${:.2f}\033[m em dólares é \033[4;36mUS${:.2f}\033[m'.format(valor, convert_dolar))
