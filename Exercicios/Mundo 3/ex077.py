"""
Crie um programa que tenha uma tupla com varias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

lista = ('aprender', 'programar', 'linguagem', 'python', 'curso',
         'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
         'programador', 'futuro')

for n in lista:
    print(f'\nNa palavra {n.upper()} temos ', end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
