"""
Faça um programa que leia um número de 0 a 9999 e moste na tela cada um dos
digitos separados.

ex:
Digite um número: 1834

Unidade: 4
Dezena: 3
centena: 8
milhar: 1
"""

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}...')
print(f'Unidade {u}')
print(f'Dezena {d}')
print(f'Centena {c}')
print(f'Milhar {m}')

# Forma matematica de fazer sem uso dos loops
