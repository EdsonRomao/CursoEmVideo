"""
Escreva um programa que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal

Esse eu não soube resolver.
"""
num = int(input('Informe um número inteiro: '))
conversao = int(input('Escolha uma das bases para conversão: \n'
                      '(1) Converter para BINÁRIO\n'
                      '(2) Converter para OCTAL\n'
                      '(3) Converter para HEXADECIMAL\n'
                      'Sua opção: '))
if conversao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif conversao == 2:
    print(f'{num} Convertido para OCTAL é igual a {oct(num)[2:]}')
elif conversao == 3:
    print(f'{num} Convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Valor inválido, tente novamente.')

