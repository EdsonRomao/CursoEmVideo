"""
Crie um algoritmo que leia um número e mostra o seu dobro, triplo e
raiz quadrada.
"""
num = int(input('Infome um número: '))
dobro = num * 2
triplo = num * 3
raizq = num ** (1/2)
# a raiz quadrada também pode ser calculada da seguinte forma pow(num, 1/2)
print(f'O dobro é {dobro} o triplo é {triplo} a Raiz quadrada é {raizq}')
