"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só
vai parar quando o usuario digitar o valor 999. que é a condição de parada.
no final, mostre quantos número foram digitados e qual foi a soma entre eles
(desconsiderando o FLAG)
"""


cont = soma = 0
while True:
    num = int(input('Informe um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você digitou {cont} números e a soma foi {soma}')
