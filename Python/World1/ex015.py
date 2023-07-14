"""
    Escreva um programa que pergunte a quantidade de Km 
    percorridos por um carro alugado e a quantidade de dias pelos
    quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
    custa R$60 por dia e R$0.15 por Km rodado.
"""
valor_dia = 60
valor_km = 0.15
quant_dia = int(input('Insira a quantidade de dias que passou com o carro: '))
quant_km = float(input('Insira quantos Km foram rodados: '))

preco_total = (quant_dia * valor_dia) + (valor_km *  quant_km)

print('Passou \033[1;32m{}\033[m dias, o total a pagar é \033[4;33mR${:.2f}\033[m '.format(quant_dia, preco_total))