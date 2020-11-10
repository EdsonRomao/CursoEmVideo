"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
no final mostre os 10 primeiros termos dessa progressão.

PA = progressão aritmetica.
"""

# this is so hard for me, i'm mother fucker dumb it's not possible.
# I get it
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for n in range(primeiro, decimo + razao, razao):
    print(f'{n}', end=' -> ')
print('ACABOU!')

# I did'nt understand all this problem yet, but i'm getting better

