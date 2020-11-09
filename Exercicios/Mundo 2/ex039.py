"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
ano = int(input('Informe o ano de nascimento '))
idade = date.today().year - ano
if idade < 18:
    falta = 18 - idade
    print(f'Você ainda terá que se alistar, falta {falta} anos')
elif idade == 18:
    print('Essa é a hora de se alistar.')
else:
    passou = idade - 18
    print(f'Já passou do tempo do alistamento, já passou {passou} anos')



