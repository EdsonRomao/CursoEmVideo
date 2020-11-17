"""
Crie um programa onde o usuario possa digitar varios valores numeros e
cadastre-os em uma lista. Caso o numero ja exista la dentro, ele não será
adicionado.
No final, serao exibidos todos os valores únicos digitados, em ordem
crescente.
"""
lista = list()
continuar = ' '

while True:
    num = (int(input('Informe um número: ')))
    if num not in lista:
        print('Número adicionado com sucesso. ')
        lista.append(num)
    else:
        print('Já existe um este número, não será adicionado.')
    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()
    while continuar != 's' and continuar != 'n':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()
    if continuar == 'n':
        break
print(f'Os números digitados em ordem crescente são {sorted(lista)}')
