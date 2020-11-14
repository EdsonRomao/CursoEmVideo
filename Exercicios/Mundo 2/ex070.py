"""
Crie um programa que leia o nome e o preço de varios produtos.
O programa devera perguntar se o usuario vai continuar. no final
Mostre:

A) qual é o total gasto na compra
B) quantos produtos custam mais de R$ 1000
C) qual é o nome do produto mais barato.
"""
total = maior_1000 = cont = menor = 0
nome_mais_barato = ''
while True:
    print('-=' * 25)
    produto = str(input('Qual nome do produto? '))
    preco = float(input('Qual preço do produto? R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        maior_1000 += 1
    if cont == 1 or preco < menor:  # Usar cont e menor pra pegar o menor valor e não fazer a gambiarra de 9999
        menor = preco
        nome_mais_barato = produto
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        print('-=' * 25)
        break
print(f'O total é de R${total}')
print(f'O produto mais barato é {nome_mais_barato} e custou R${menor:.2f}')
print(f'há {maior_1000} produtos maior que R$1000 ')
