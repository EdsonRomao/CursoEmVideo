"""
Faça um programa que leia UM NÚMERO qualquer e mostre o seu fatorial.

ex:
5! = 5x4x3x2x1 = 120

# Python way

from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')

# using while

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

"""
from time import sleep
num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = 1
print(f'Calculando {num}! = ', end='')
sleep(2)
for n in range(1, num):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')


