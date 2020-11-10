"""
Crie um programa que leia VARIOS NUMEROS inteiros pelo teclado.
no final da execução, mostre a media entre todos os valores e qual foi
o maior e o menor valores lidos.
O programa deve perguntar ao usuario se ele quer ou não continuar a
digitar valores.
"""

maior = 0
menor = 0
media = 0
soma = 0
n = -1
cont = 0
while n != 0:
    n = int(input("Digite um número: "))
    soma += n
    cont += 1
    media = soma / cont
    if n == 1:
        maior += n
        menor += n
    if n < menor:
        menor = n
    if n > maior:
        maior = n
    if n == 0:
        cont = cont - 1

'''   if continuar == 'S':
        n = int(input('Digite um número: '))
    if continuar == 'N':'''

print(f'A media entre os números foi {media}')
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitador foi {menor}')
