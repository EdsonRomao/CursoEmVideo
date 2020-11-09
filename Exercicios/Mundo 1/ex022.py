"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todas as letras maiúsculas
> O nome com todas as letras minúsculas
> Quantas letras ao todo (sem considerar os espaços)
> quantas letras tem o primeiro nome.
"""
nome = str(input('Informe seu nome completo: ')).strip()
print('Analisando seu nome....')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print('Seu nome ao todo tem {} letras.'.format(len(nome) - nome.count(' ')))
dividido = (nome.split())
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0], len(dividido[0])))
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras.')
