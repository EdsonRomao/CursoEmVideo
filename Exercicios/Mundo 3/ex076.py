"""
Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequencia.

No final, mostre uma listagem de preços, organizando os dados em forma tabulas.

"""
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Compasso', 9.99,
            'Mochila', 132.99,
            'Canetas', 15.99,
            'Livro', 23.9)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for n in range(0, len(listagem)):
    if n % 2 == 0:
        print(f'{listagem[n]:.<30}', end='')
    else:
        print(f'R${listagem[n]:>7.2f}')
print('-' * 40)