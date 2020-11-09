"""
Escreva um programa que pergunte o salário de um funcionario e calcule
o valor do seu aumento.

Para salários superiores a R$1.250,00 calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de 15%

"""

salario = float(input('Informe seu sálario atual: '))
if salario <= 1250:
    aumento15 = (salario / 100) * 15 + salario
    print(f'O seu sálario de {salario:.2f} irá para {aumento15:.2f}, com 15% de aumento.')

else:
    aumento10 = (salario / 100) * 10 + salario
    print(f'O seu sálario de {salario} irá para {aumento10}, com 10% de aumento.')

