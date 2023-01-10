# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do 
# Campeonato Brasileiro de Futebol 2019, na ordem de colocação. Depois Mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os ultimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabetica.
# D) Em que posição na tabela está o time "Chapecoense" 
tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo',
'Internacional','Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG',
'Fluminense', 'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí' )
enfeite = '-='*20
print(f'Lista de times do Brasileirão: {tabela}\n', enfeite)
print(f'Os 5 primeiros colocados: {tabela[0:5]}\n', enfeite)
print(f'Os 4 ultimos colocados: {tabela[-4:]}\n', enfeite)
print(f'Em ordem alfabetica: {sorted(tabela)}\n', enfeite)
print(f"O time Chapecoense está na posição {tabela.index('Chapecoense')+1} da tabela\n", enfeite)
