"""
faça um programa que leia 5 valores númericos e guarde-os em uma lista.

No final, mostre qual foi o MAIOR e o MENOR valor digitado e as suas
respectivas posições na lista.
"""

num = list()
maior = menor = 0

for cont in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = num[cont]
    else:
        if num[cont] > maior:
            maior = num[cont]
        if num[cont] < menor:
            menor = num[cont]
print('-=' * 30)
print(f'Você digitou os valores {num}')
print(f'O maior valor que encontrei foi {maior} nas posições ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor que encontrei foi {menor} nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
print()


