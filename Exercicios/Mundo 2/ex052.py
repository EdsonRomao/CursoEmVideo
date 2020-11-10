"""
Faça um programa que leia um número inteiro e diga se ele é ou não um
número primo.

numero primo: Só é número primo um número que SOMENTE pode ser dividido por 1 ou por ele mesmo.
"""
# Fiquei inrrolado neste exercicio.

num = int(input('Digite um número: '))
tot = 0
for n in range(1, num + 1):
    if num % n == 0:
        print('\33[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print(f'{n}', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes ')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
