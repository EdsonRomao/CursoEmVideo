"""
Crie um programa que leia VARIOS números inteiros pelo teclado.
O programa só vai parar quando o usuario digitar o valor 999, que é
a CONDIÇÃO DE PARADA. no final, mostre quantos números foram digitados e
qual foi a soma entre eles.
(desconsiderando o FLAG, 999)

while num != 999:
    num = int(input('Informe o número: '))
    soma += num
    cont += 1
    if num == 999:
        soma -= 999
        cont -= 1
print(f'Foram digitados {cont} números.')
print(f'A soma entre todos números digitados é {soma}')
"""
# posso simplificar as vareaveis assim soma = cont = num = 0
soma = num = cont = 0
num = int(input('Informe o número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Informe o número: '))
print(f'Foram digitados {cont} números.')
print(f'A soma entre todos números digitados é {soma}')
