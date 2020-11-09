"""
Faça um algortmo que leia o salário de um funcinário e mostre seu novo
salário, com 15% de aumento.
"""
salario = float(input('Informe qual seu sálario: '))
aumento = (salario / 100) * 15 + salario
print(f'Seu salário com 15% de aumento vai para {aumento:.2f} Reais.')
