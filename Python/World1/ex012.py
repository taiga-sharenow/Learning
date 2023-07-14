"""
    Faça um algoritmo que leia o preço de um produto e mostre seu 
    novo preço, com 5% de desconto.
"""
valor_deconto = 5
preco_prod = float(input('Insira o valor do produto: '))

desc_preco = preco_prod * valor_deconto / 100
novo_preco = preco_prod - desc_preco

print(f'O valor do produto com o desconto de \033[4;31m{valor_deconto}%\033[m, o valor do desconto no produto é \033[4;31mR${desc_preco}\033[m, aplicado é: \033[4;31mR${novo_preco}\033[m')