"""
Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada
valor digitado pelo usuario. O programa será interrompuido quando o número solicitado for
NEGATIVO.
"""
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('=-' * 20)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c} ')
    print('-=' * 20)


print('Programa tabuada encerrado. voltei always!')

# Travei nesse exercicio, eu simplesmente não consegui mostrar a proxima tabuada.
