"""
A confederação nacional de natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:

- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 25 anos: SENIOR
- acima : MASTER
"""
from datetime import date
nascimento = int(input('Informe o ano de seu nascimento: '))
idade = date.today().year - nascimento

if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif 19 > idade <= 25:
    print('SENIOR')
else:
    print('MASTER')

