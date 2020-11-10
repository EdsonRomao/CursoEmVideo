"""
crie um programa que leias DOIS VALORES e mostre um menu na tela:

[1] Somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

seu programa deverá realizar a operação solicitada em cada caso.
"""

num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
soma = num1 + num2
mult = num1 * num2
maior = 0
opcao = ''
while opcao != '5':
    opcao = str(input('O que deseja fazer com os números digitados: \n'
                      '[1] Somar\n'
                      '[2] multiplicar\n'
                      '[3] Mostrar maior\n'
                      '[4] Novos números\n'
                      '[5] Sair do Programa\n'
                      'Qual a opção: '))
    if opcao == '1':
        print(f'O resultado da soma é {soma}.')
    if opcao == '2':
        print(f'O resultado da multiplicação é {mult}')
    if opcao == '3':
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior número é {maior}')
    if opcao == '4':
        num1 = int(input('Informe o primeiro valor: '))
        num2 = int(input('Informe o segundo valor: '))
print('FIM')
