"""
faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto
"""
p = float(input('Informe o preço do produto: '))
d = (p / 100) * 5
pd = p - d
print(f'O preço deste produto com 5% de desconto é {pd:.2f} reais. ')
