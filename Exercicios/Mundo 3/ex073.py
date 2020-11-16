"""
Crie uma tupla preenchida com os 20 primeiros colocaados da tabela do
campeonato brasileiro de futebol, na ordem de colocação. depois mostre:

A) apenas os 5 primeiros colocados
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabetica.
D Em que posição na tabela está o time da chapecoense.
"""

times = ('Atletico-MG', 'Internacional', 'São paulo', 'Flamengo', 'Palmeiras', 'Santos', 'Grêmio',
         'Fluminense', 'Bahia', 'Chapecoense', 'Corinthians', 'Fortaleza', 'Ceará', 'Atlético-GO',
         'Vasco da Gama', 'Athletico-PR', 'Coritiba', 'Bragantino-SP', 'Botafogo', 'Goiás')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos  são: {times[-4:]} ')
print('-=' * 20)
print(f'Times em ordem alfabétida {sorted(times)}')
print('-=' * 20)
print(f'O chapecoense está na {times.index("Chapecoense")+1}º posição')



