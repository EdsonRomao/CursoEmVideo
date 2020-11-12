"""
crie um programa que leias DOIS VALORES e mostre um menu na tela:

[1] Somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep
num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
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
    print('Calculando aguarde...')
    sleep(1)
    if opcao == '1':
        soma = num1 + num2
        print('-' * 25)
        print(f'A soma entre {num1} + {num2} é {soma}.')
        print('-' * 25)
    if opcao == '2':
        mult = num1 * num2
        print('-' * 25)
        print(f'O resultado de {num1} x {num2} é {mult}')
        print('-' * 25)
    if opcao == '3':
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('-' * 25)
        print(f'Entre {num1} e {num2} o maior valor é {maior}')
        print('-' * 25)
    if opcao == '4':
        num1 = int(input('Informe o primeiro valor: '))
        num2 = int(input('Informe o segundo valor: '))
    sleep(2)
print('FIM')
