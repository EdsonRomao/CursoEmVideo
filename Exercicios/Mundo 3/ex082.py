"""
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vao conter apenas os valores
pares e os valores impares digitados, respectivamente.

ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
pares = []
impares = []
while True:
    n = int(input('Informe um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = ' '
    while continuar != 's' and continuar != 'n':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()
    if continuar == 'n':
        break
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números impares é {impares}')

