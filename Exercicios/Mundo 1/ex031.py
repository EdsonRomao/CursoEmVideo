"""
Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0.50 por km para viagens até 200km
e R$0.45 para viagens mais longas
"""
km = float(input('Qual a distância da sua viagem: '))
if km <= 200:
    km = km * 0.50
    print(f'A sua viagem será R${km} considerando R$0.50 por KM')
else:
    km = km * 0.45
    print(f'A sua viagem ficara R$ {km} considerando R$0.45 por KM')

