"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média antingida:

- média abaixo de 5.0:
Reprovado
- média entre 5.0 e 6.9:
Recuperação
- média 7.0 ou superior:
Aprovado
"""
nota = float(input('Informe a primeira nota: '))
nota1 = float(input('Informe a segunda nota: '))
media = (nota + nota1) / 2

if media < 5.0:
    print('REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO!')
elif media > 7.0:
    print('APROVADO!')
