"""
Faça um programa que leia o peso de cinco pessoas. no final, mostre qual
foi o maior e o menor peso lidos.
"""

maior = 0
menor = 999

for n in range(1, 6):
    peso = float(input(f'Informe o {n}º peso em (kg) : '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso foi {maior}kg')
print(f'E o menor peso foi {menor}kg')
