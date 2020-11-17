"""
Crie um programa que vai ler varios números e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados.

B) a lista de valores, ordenada de forma decrescente.

C) se o valor 5 foi digitado e está ou não na lista
"""
lista = []
continuar = ' '
while True:
    n = int(input('Informe um número: '))
    lista.append(n)
    continuar = str(input('Quer continuar? [S/N} ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N} ')).upper().strip()
    if continuar == 'N':
        break
print(f'Você digitou {len(lista)} elementos! ')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista} ')
if 5 in lista:
    print('O valor 5 faz parte da lista! ')
else:
    print('O valor 5 NÃO foi encontrado!')
