"""
Faça um programa que leia o comprimeto do cateto oposto e do cateto adjacente de
um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

# Exemplo 1
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')

"""

# Exemplo 2
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')
