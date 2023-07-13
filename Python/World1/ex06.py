"""
    Crie um algoritmo que leia um número e mostre o seu dobro, triplo e 
    raiz quadrada
"""
import numpy

value = float(input("Digite um valor: "))
dobro = value * 2
triplo = value * 3
raiz = numpy.sqrt(value)
print(f'O dobro do valor digitado é: \033[1m{dobro}\033[m')
print(f'O triplo do valor digitado é: \033[1m{triplo}\033[m')
print(f'A raiz do valor digitado é: \033[1m{raiz:.2f}\033[m')
