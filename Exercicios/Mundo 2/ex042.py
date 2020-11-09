"""
Refaça o desafio 035 dos trinagulos acrescentando o recurso de mostrar
que tipo de triangulo será formado:

- Equilátero: Todos os lados iguais
- isósceles: dois lados iguais
- Escaleno: todos os lados diferentes

a = b
a = c
b = c

"""

a = int(input('Informe o primeiro comprimento: '))
b = int(input('Informe o segundo comprimento: '))
c = int(input('Informe o terceiro comprimento: '))

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print('Os comprimentos formam um Triângulo Equilátero.')
    elif a != b and b != c and c != a:
        print('Os comprimentos formam um Triângulo Escaleno.')
    else:
        print('Os comprimentos formam um Triângulo Isósceles.')
else:
    print('Os comprimentos acima NÃO PODEM formar um triângulo.')

# Me inrrolei muito na parte dos isósceles pois eram muitas comparações que eu teria de fazer,
# mas com exemplo que foi dado se não for equilátero nem escaleno, automaticamente sera isosceles,
# Muito bom saber disso, poupou varias horas de rachamento de cabeça.
