"""
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador.

O programa deverá escrever na tela se o usúario venceu ou perdeu

from random import choice
print('Estou pensando em um número um momento....')
n = [1, 2, 3, 4, 5]
a = (choice(n))
num = int(input('Tente adivinhar qual número eu pensei de 0 a 5: '))
if a == num:
    print('ACERTO MIZERAVI')
else:
    print(f'ERROUUUUUUUUU O número correto era {a}')"""

# outra forma
from random import randint
from time import sleep
computador = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO AGUARDE....')
sleep(1)
if jogador == computador:
    print('PARABÈNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no número {jogador}')

