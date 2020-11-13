"""
Crie um programa que leia VARIOS NUMEROS inteiros pelo teclado.
no final da execução, mostre a media entre todos os valores e qual foi
o maior e o menor valores lidos.
O programa deve perguntar ao usuario se ele quer ou não continuar a
digitar valores.
"""

media = menor = maior = cont = soma = 0
continuar = 'S'

while continuar in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
media = soma / cont
print(f'você digitou {cont} números e a média foi {media}')
print(f'O maior número é {maior} e o menor {menor}')

