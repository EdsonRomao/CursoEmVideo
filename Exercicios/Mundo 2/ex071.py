"""
Crie um programa que simule o funcionamento de um caixa eletronico.
no inicio, pergunte ao usuario qual sera o valor a ser sacado
(numero inteiro) e o programa vai informar quantas cédulas de cada valor
serão entregues.

OBS: Considere que o caixa possui cédulas de R$ 50, R$20 R$10 e R$1
"""
print('-=' * 30)
print('{:^30}'.format('BANCO ROMAO'))
print('-=' * 30)
valor = int(input('Qual valor deseja sacar? R$ '))
total = valor
notas = 50
tot_notas = 0
while True:
    if total >= notas:
        total -= notas
        tot_notas += 1
    else:
        if tot_notas > 0:
            print(f'Total de {tot_notas} de R${notas}')
        if notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 1
        tot_notas = 0
        if total == 0:
            break


# Tive dificuldade para entender a logíca desse exercicio, volto dias mais tarde para ver.
