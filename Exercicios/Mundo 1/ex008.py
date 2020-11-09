"""
Escreva um programa que leia um valor em metros e o exiba convertido,
em centimetros e milímetros.
"""


m = float(input('Informe o valor em metros: '))
cen = m * 100
mi = m * 1000
print(f'{m} metros é igual a {cen} centimetros e {mi} milimetros')
