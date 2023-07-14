"""
    Faça um programa que leia a largura e a altura de uma parede em
    metros, calcule a sua área e a quantidade de tinta necessária para
    pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""
altura = float(input('Qual a altura da parede, em metros? '))
largura = float(input('Qual a largura da parede, em metros? '))

area = altura * largura
litro_tinta = area /2

print(f'\033[4mPara uma parede de {area} m² é necessário {litro_tinta} L de tinta.\033[m')