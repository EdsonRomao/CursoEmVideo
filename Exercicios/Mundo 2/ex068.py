"""
Faça um programa que jogue par ou impar com o computador. O jogo só será
interrompido quando o jogador perder.
mostrando o total de vitorias consecutivas que ele conquistou no final
do jogo.
"""
from random import randint
soma = 0
print('-=' * 20)
print('JOGO PAR OU IMPAR!')
print('-=' * 20)
cont = 0
while True:
    computador = randint(1, 11)
    jogador = int(input('Digite um valor: '))
    escolha = str(input('Par ou Impar [P/I] '))
    print('-' * 20)
    soma = computador + jogador
    if escolha in 'Pp':
        if soma % 2 == 0:
            cont += 1
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
            print('--' * 20)
            print(f'Jogador ganhou')
            print('--' * 20)
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU IMPAR')
            print('--' * 20)
            print(f'Computador ganhou.')
            print('-=' * 20)
            break
    if escolha in 'iI':
        if soma % 2 == 1:
            cont += 1
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU IMPAR')
            print('--' * 20)
            print(f'Jogador ganhou')
            print('--' * 20)
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
            print('--' * 20)
            print(f'Computador ganhou!')
            print('-=' * 20)
            break
print(f'GAME OVER! Você teve {cont} vitorias consecutivas')

