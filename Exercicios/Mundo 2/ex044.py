"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de JUROS
"""
preco = float(input('Qual o valor do produto? '))
condicao = str(input('Como deseja pagar? Opçoes abaixo. \n'
                     '(1) A vista dinheiro.\n'
                     '(2) A vista cartão.\n'
                     '(3) Em até 2x cartão.\n'
                     '(4) 3x ou mais no cartão.\n'
                     'Digite a opção desejada: '))

desconto10 = (preco / 100) * 10
desconto5 = (preco / 100) * 5
juros20 = (preco / 100) * 20

if condicao == '1':
    print(f'O produto que era R${preco} com 10% de desconto será R${preco - desconto10}')
elif condicao == '2':
    print(f'O produto que era R${preco} com 5% de desconto será R${preco - desconto5}')
elif condicao == '3':
    print(f'Parcelando no cartão até 2x não terá juros o valor R${preco} em 2x de R${preco / 2} ')
elif condicao == '4':
    print(f'Parcelando em 3x ou mais terá um acrescimo de 20% de juros, o valor de {preco} irá para {preco + juros20}')
else:
    print('A opção escolhida não é valida, cheque o número correto! ')
