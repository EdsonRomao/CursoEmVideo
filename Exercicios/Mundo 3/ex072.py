"""
Crie um programa que tenha uma tupla totalemente preenchida com uma contagem
por extenso, de zero até vinte.

seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrálo por extenso.
"""

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))
while True:
    if num > 20 or num < 0:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        break
print(f'Você digitou o numero {numeros[num]}')


