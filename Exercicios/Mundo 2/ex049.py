"""
refaça o desafio 009, mostrando a tabuada de um número que o usuario escolher,
so que agora utilizando um laço for.
"""
num = int(input('Infome o número da tabuada que deseja ver: '))

for n in range(1, 11):
    soma = n * num
    print(f'{num} x {n} = {soma}')

