"""
Melhore o jogo do desafio 028 aonde o computador vai "pensar" em um número entre
0 e 10. só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
"""

from random import randint
from time import sleep
computador = randint(0, 11)
cont = 1
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('PERA DEIXA EU PENSAR...')
sleep(1)
jogador = int(input('Em que número eu pensei? '))
while jogador != computador:
    jogador = int(input('Errou tente novamente! '))
    cont += 1
if jogador == computador:
    print('VOCÊ VENCEU!!!!')
    print(f'Você acertou em {cont} palpites.')
