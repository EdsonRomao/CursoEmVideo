"""
Melhore o desafio 061, pergutando para o usuario mais alguns termos.
O programa encerra quando ele disse que quer mostras os TERMOS.

primeiro = int(input('Primeiro termo: '))  # input to know what number will start
razao = int(input('Razão: '))  # input to know how many numbers will jump
termo = primeiro  # term to keep the numbers
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais? '))
print(f'Progresso finalizado com {total} termos mostrados. ')

"""

primeiro = int(input('Informe o termo: '))
razao = int(input('Informe a razão: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Mais quantos termos deseja ver? '))
print(f'Progresso finalizado com {total} de termos mostrados.')




