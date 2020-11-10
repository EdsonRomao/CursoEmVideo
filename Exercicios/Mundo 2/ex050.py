"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. se o valor digitado for IMPAR, desconsidere-o
"""
par = 0
for n in range(1, 7):
    num = int(input('Escolha os números: '))
    if num % 2 == 0:
        par += num
print(par)
# O de cima foi a minha soolução

# Solução do professor

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {soma}')
