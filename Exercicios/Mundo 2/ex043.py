"""
Desenvolva umas lógica que leia o peso e a altura de uma pessoas,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade morbida.
"""
altura = float(input('Qual a sua altura: '))
peso = float(input('Qual seu peso atual: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Abaixo do peso seu IMC é {imc:.2f}')
elif imc >= 18.5 and imc < 25:
    print(f'Você está no seu peso ideal seu IMC é {imc:.2f}')
elif imc >= 25 and imc < 30:
    print(f'Você está com sobrepeso, seu IMC é {imc:.2f}')
elif imc >= 30 and imc < 40:
    print(f'Você está com obesidade, seu IMC é {imc:.2f}')
else:
    print(f'Você está com Obesidade Morbida seu IMC é {imc:.2f}')
