"""
Escreva um programa que leia a velocidade de um carro.

se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
foi multado

A multa vai custar R$7,00 por km acima do limite
"""
ve = int(input('Informe a velocidade que passou pelo radar: '))
if ve > 80:
    multa = (ve - 80) * 7
    print(f'Você será multado em R${multa:.2f}')
else:
    print(f'Parabéns você respeitou a velocidade.')
