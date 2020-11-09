"""
Escreva um origrama que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que
o carro custa R$60 por dia e R$0.15 por km rodado.
"""
d = int(input('Por quantos dias alugou o veiculo? '))
km = float(input('Quantos km foram rodados? '))
custo_total = (d * 60) + (km * 0.15)
print(f'O total a pagar é R${custo_total:.2f}')
