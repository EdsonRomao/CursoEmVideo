"""
Crie um programa que leia o ano de nascimento de sete  pessoas, no final, mostre
quantas pessoas ainda não antigiram a maioridade e quantas pessoas já são maiores.
"""
from datetime import date
maior = 0
menor = 0
for n in range(1, 8):
    ano = int(input(f'Em que ano a {n}º pessoa nasceu: '))
    idade = date.today().year - ano
    if idade < 18:
        menor += + 1
    if idade >= 18:
        maior += + 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'E também tivemos {menor} pessoas menores de idade.')

