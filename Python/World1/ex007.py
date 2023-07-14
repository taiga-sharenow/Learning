"""
    Desenvolva um programa que leia as duas notas de um aluno,
    calcule e mostre a sua média    
"""

nota_1 = float(input('Insira a nota do primeiro bimestre: '))
nota_2 = float(input('Insira a nota do segundo bimestre: '))

media = (nota_1 + nota_2) / 2

print(f'A média do aluno foi: \033[1;33m{media}\033[m')