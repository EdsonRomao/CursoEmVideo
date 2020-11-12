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


# Exemplo professor
from random import randint
computador = randint(0, 10)
print('Sou seu compuador... acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
