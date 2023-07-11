"""
    Escreva um 
    programa para aprovar 
    o empréstimo bancário 
    para a compra de uma 
    casa. O programa vai
    pergutnar o valor da
    casa, o salário do 
    comprador e em 
    quantos anos ele vai
    pagar.
    
    Calcule o valor da
    prestação mensal,
    sabendo que ela não
    pode exceder 30% do
    salário ou então o
    empréstimo será
    negado
"""
#Datas
house_price = float(input('Qual o valor da casa? '))
salary = float(input('Qual o seu salário? '))
years_pay = int(input('Em quantos anos você irá pagar? '))

#Calculate
mensal_prest = house_price / (years_pay * 12)
verify_salary = salary * 30 /100

#Text
print(f'Para pagar uma casa de R${house_price:.2f} em {years_pay}')
print(f' a prestação será de R${mensal_prest:.2f}')

#Conditions
if mensal_prest <= verify_salary :
    print('Aprovado!')
else : 
    print('Negado!')



