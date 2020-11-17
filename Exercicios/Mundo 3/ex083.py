"""
Crie um programa onde o usuario digite uma expressão qualquer que use
parenteses. seu aplicativo deverá analisar se a expressao passada está
com os parenteses abertos e fechados na ordem correta.
"""
expr = str(input('Digite a expressão: '))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está CORRETA!')
else:
    print('Sua expressão está INVÁLIDA!')
