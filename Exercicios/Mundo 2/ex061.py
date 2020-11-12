"""
Refaça o desafio 051, lendo o PRIMEIRO TERMO e a RAZAO de uma PA, mostrando os
10 primeiros termos da progressão usando a estrutura while.
"""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1


while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')
