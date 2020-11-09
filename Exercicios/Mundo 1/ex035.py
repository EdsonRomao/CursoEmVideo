"""
desenvolva um programa que leia o comprimento de três retas e diga ao usuarios
se elas podem ou não formar um triangulo.
"""
a = int(input('Informe o primeiro comprimento: '))
b = int(input('Informe o Segundo comprimento: '))
c = int(input('Informe o terceiro comprimento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os comprimentos acima PODEM FORMAR triângulos!')
else:
    print('Os comprimentos acima NÂO PODEM formar triangulo.')

