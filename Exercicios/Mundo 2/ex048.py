"""
Faça um programa que calcule a soma entre todos os números impares que são
multiplos de três e que se encontram no intervalo de 1 até 500.

num1 = 0

for n in range(1, 501):
    if n % 2 == 1:
        num =+ n
        if num % 3 == 0:
            num1 = num1 + num
print(f'A soma de todos os número multiplos de 3, é {num1}')
"""


soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma dos {cont} números, é {soma}!')
