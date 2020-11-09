"""
Crie um programa que leia um nome de uma cidade e diga se ela começa ou não
com o nome "SANTO"
"""
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')



