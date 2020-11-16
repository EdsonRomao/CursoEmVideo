"""
Crie um programa que vai gerar cinco números aleatorios e colocar em uma tupla.

Despois disso, mostre a listagem de números gerados e tambem indique o menor e o
maior valor que estão na tupla.

"""
from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10))
print('Os valors sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')

