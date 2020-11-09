"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar.

Considere US$1,00 = R$3,27
"""
real = float(input("Quantos reais tem na carteira? "))
dolar = real / 3.27
print(f'Com essa contia você pode comprar {dolar:.2f} Dólares. ')

