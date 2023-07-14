"""
    Escreva um programa que leia um valor em metros e exiba
    convertido em centímetros e milímetros.    
"""
m = float(input('Digite um valor em metros: '))

cm = m * 100
mm = m * 1000

print('A medida de \033[1m{} m\033[m em centímetros é \033[1m{} cm\033[m'.format(m, cm)) 
print('A medida de \033[1m{} m\033[m em milímetros é \033[1m{} cm\033[m'.format(m, mm)) 