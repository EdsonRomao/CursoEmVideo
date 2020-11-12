"""
Vamos tentar fazer um simulador de uma prova de historia

while opcao != 6:
    opcao = int(input('Escolha a opção abaixo:\n'
                      '[1] Pergunta um\n'
                      '[2] Pergunta dois\n'
                      '[3] Pergunta três\n'
                      '[4] pergunta quatro\n'
                      '[5] Ver Resultado!\n'
                      '[6] Sair do programa!\n'
                      'Qual opçãod deseja: '))


if opcao == 1:

"""
from time import sleep
print('==' * 20)
print('Bem vindo a sua prova de historia geral!!')

resposta1 = 0
certa = 0
errada = 0
resposta2 = 0
resposta3 = 0
resposta4 = 0
tot = 4
opcao = 0
passou = 0

print('==' * 20)
resposta1 = int(input('A chamada civilização helenística iniciou-se:\n'
                      '[1] com o domínio espartano sobre Atenas\n'
                      '[2] com a revolução filosófica de Platão\n'
                      '[3] com a união das culturas grega e persa\n'
                      '[4] com a formação do império de Alexandre Magno\n'
                      'Qual a opção correta? '))
print('==' * 20)
if resposta1 == 1:
    certa += 1
else:
    errada += 1

resposta2 = int(input('A frase “O Egito é o presente do Nilo” é atribuída a:\n'
                      '[1] Hipócrates\n'
                      '[2] Heródoto\n'
                      '[3] Sócrates\n'
                      '[4] Platão\n'
                      'Qual opção: '))
print('==' * 20)
if resposta2 == 1:
    certa += 1
else:
    errada += 1

resposta3 = int(input('Chamado de “A Raposa do Deserto” durante a II Guerra Mundial foi:\n'
                      '[1] Pétain\n'
                      '[2] Rommel\n'
                      '[3] Átila\n'
                      '[4] Bismarck\n'
                      'Qual opção: '))
print('==' * 20)
if resposta3 == 1:
    certa += 1
else:
    errada += 1

resposta4 = int(input('A civilização mesopotâmica desenvolveu-se no vale dos rios:\n'
                      '[1] Tigre e Nilo\n'
                      '[2] Tigre e Eufrates\n'
                      '[3] Eufrates e Ganges\n'
                      '[4] Nilo e Indus\n'
                      'Qual opção? '))
print('==' * 20)
if resposta4 == 1:
    certa += 1
else:
    errada += 1

passou = (certa / tot) * 100
print('Calculando...')
sleep(2)
if passou > 70:
    print(f'Parabens você passou! com {passou}% de acerto! ')
    print('==' * 20)

else:
    print(f'Infelizmente você não passou a sua media foi de {passou}%.')
    print('==' * 20)
print('FIM')
