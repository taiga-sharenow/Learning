"""
    Faça um programa
    que leia o ano de
    nascimento de um
    jovem e informe, de
    acordo com sua idade:
    
    -Se ele ainda vai se
    alistar ao serviço
    militar.
    -Se é a hora de se
    alistar
    -Se já passou do
    tempo do alistamento
    
    Seu programa também 
    deverá mostrar o 
    tempo que falta ou 
    que passou do prazo.   
"""
from datetime import date

birth_year = int(input('Qual a sua idade?'))
today_year = int(date.today().year)

age = today_year - birth_year

print('Sua idade é: {}'.format(age), end='|')

if age < 18 :
    years_for = 18 - age
    print(f'Ainda vai se alistar ao serviço militar, daqui a {years_for}')
elif age == 18 :
    print('É a hora de se alistar!')
else :
    years_after = age - 18
    print(f'Já passou {years_after} anos do tempo de alistamento')


