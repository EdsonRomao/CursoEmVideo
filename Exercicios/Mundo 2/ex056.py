"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
no final do programa, mostre:

- A média de idade do grupo
- qual é o nome do homem mais velho
- quantas mulheres tem menos de 20 anos.
"""
soma = 0
media = 0
idade_mais_velho = 0
mulher_menos_20 = 0
nome_mais_velho = ''
for n in range(1, 5):
    print(f'----- {n}º PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma = soma + idade
    if n == 1 and sexo in 'Mm':
        idade_mais_velho = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_menos_20 += 1
media = (soma / 4)
print(f'A média do grupo é {media} anos.')
print(f'O homen mais velho é o {nome_mais_velho}')
print(f'há {mulher_menos_20} mulheres abaixo de 20 anos.')

# Tentei por mais de 1 hora e não achei a solução, ele sempre pega o último nome, e eu não consigo substituir,
# Não consigo subistituir o Nome.
# depois de 2 horas achamos a solução ta ficando hard.
