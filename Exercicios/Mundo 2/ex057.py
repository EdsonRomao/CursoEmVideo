"""
Faça um programa que leia o SEXO de uma pessoa, mas só aceite
os valor 'M' ou 'F'. caso esteja errado peça a digitação novamente até
ter um valor correto.
"""
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o seu sexo? [M/F] ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('Dados inválidos. Por favor, informe seu sexo: ')
    else:
        print(f'Sexo {sexo} registrado com sucesso.')
print('FIM')

# Outra forma seria
sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
