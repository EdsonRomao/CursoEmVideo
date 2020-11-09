"""
Escreva um programa para aprovar o emprestimo bancario para a compra de
uma casa. O programa vai perguntar o VALOR DA CASA, o SALARIO DO COMPRADOR
e em QUANTOS ANOS ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder
30% do sálario ou então o emprestimo será negado.
"""
valor = float(input('Informe o valor que deseja financiar: '))
salario = float(input('Quantos é o seu sálario mensal: '))
anos = float(input('Quantos anos você deseja financiar? '))

maximo = (salario / 100) * 30
parcela = (valor / anos) / 12
if parcela > maximo:
    print('Emprestimo negado, o valor não pode ultrapassar 30% do seu sálario.')
    print(f'O valor máximo que você pode pagar é R${maximo:.2f}')
    print(f'E o valor dessa parcela ficaria R${parcela:.2f}')
else:
    print(f'O emprestimo foi concebido o valor da parcela será {parcela:.2f}')

