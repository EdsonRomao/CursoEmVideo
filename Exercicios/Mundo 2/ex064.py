"""
Crie um programa que leia VARIOS números inteiros pelo teclado.
O programa só vai parar quando o usuario digitar o valor 999, que é
a CONDIÇÃO DE PARADA. no final, mostre quantos números foram digitados e
qual foi a soma entre eles.
(desconsiderando o FLAG, 999)
"""

soma = 0
num = 0
cont = 0
while num != 999:
    num = int(input('Informe o número: '))
    soma += num
    cont += 1
    if num == 999:
        soma -= 999
        cont -= 1
print(f'Foram digitados {cont} números.')
print(f'A soma entre todos números digitados é {soma}')
