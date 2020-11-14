"""
Crie um programa que leia a idade e o sexo de varias pessoas. a cada
pessoa cadastrada, o programa deverá perguntar se o usuario quer ou não
continuar, no final mostre:

A) quantas pessoas tem mais de 18 anos
B) quantos homens foram cadastrados
C) quantas mulheres tem menos de 20 anos.

"""
maior_18 = homem = mulher_menos_20 = 0
while True:
    print('-=' * 20)
    print('CADASTRE UMA PESSOA!')
    print('-=' * 20)
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo? [M/F] ')).upper().split()[0]
    print('-=' * 20)
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Qual seu sexo? [M/F] ')).upper().split()[0]
    if idade >= 18:
        maior_18 += 1
    if sexo in 'M':
        homem += 1
    if idade < 20:
        if sexo in 'F':
            mulher_menos_20 += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas maiores que 18 anos: {maior_18}')
print(f'Total de homens cadastrados: {homem}')
print(f'Total de mulheres menores de 20 anos: {mulher_menos_20}')


