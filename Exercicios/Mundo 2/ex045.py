"""
Crie um programa que faça o computador jogar Jokenpô com você.
Pedra, papel e tesoura.

pedra ganha tesoura
pedra perde pra papel
papel perde pra tesoura


"""
import random
from time import sleep
print('Vamos jogar JOKENPÔ? ')
lista = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(lista)
jogador = str(input('Escolha um:\n'
                    'Pedra\n'
                    'Papel\n'
                    'Tesoura\n'
                    'Qual sua escolha: ')).upper().strip()
print('Ok, vamos lá!')
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(1)
if jogador == 'PEDRA' and computador == 'Tesoura':
    print(f'Você ganhou eu escolhi {computador} e você {jogador}')
elif jogador == 'PEDRA' and computador == 'Papel':
    print(f'Eu ganhei eu escolhi {computador} e você {jogador}')
elif jogador == 'PAPEL' and computador == 'Tesoura':
    print(f'Você perdeu, eu escolhi {computador} e você {jogador}')
elif jogador == 'PAPEL' and computador == 'Pedra':
    print(f'Você ganhou, eu escolhi {computador} e você {jogador}')
elif jogador == 'TESOURA' and computador == 'Pedra':
    print(f'Eu ganhei, eu escolhi {computador} e você {jogador}')
elif jogador == 'TESOURA' and computador == 'Papel':
    print(f'Você ganhou, eu escolhi {computador} e você {jogador}')
elif jogador == 'TESOURA' and computador == 'Tesoura':
    print(f'EMPATE! Ambos escolhemos {jogador}  ')
elif jogador == 'PAPEL' and computador == 'Papel':
    print(f'EMPATE! Ambos escolhemos {jogador}')
elif jogador == 'PEDRA' and computador == 'Pedra':
    print(f'EMPATE! Ambos escolhemos {jogador}')
else:
    print('Valor incorreto, por favor escolha uma das opções acima: ')




