"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
ordem = sorted(lista)
print(f'A ordem dos alunos é {ordem}')

# Pode ser usado a função random.shuffle tambem
