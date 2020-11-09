"""
Escreva um programa que leia dois numero inteiros e compare-os
mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- não existe valor maior, os dois são iguais
"""
numero = int(input('Informe o primeiro número: '))
numero1 = int(input('Informe o segundo número: '))

if numero > numero1:
    print(f'O primeiro número é maior {numero} do que o segundo {numero1}')
elif numero1 > numero:
    print(f'O segundo número é maior {numero1} do que o primeiro {numero}')
else:
    print(f'Não existe valor maior, os dois são iguais. {numero} e {numero1}')
