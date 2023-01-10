'''Aprimore o Desafio 093 para que ele funcione com varios jogadores, 
incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.'''
player = {}
time = []
gols = []
cont = ''
while cont != 'N':
    print('-'* 45)
    player['nome'] = str(input('Nome do Jogador: ')).title()
    qnt_p = int(input(f'Quantas partidas {player["nome"]} jogou? '))
    for c in range(1, qnt_p +1):
        gols.append(int(input(f'Quantos gols {player["nome"]} marcou na {c}° partida? ')))
    player['gols'] = gols[:]
    time.append(player.copy())
    gols.clear()
    while True:
        cont = str(input('Quer continuar?[S/N]  ')).upper().strip()[0]
        if cont not in 'SN':
            print('Erro! Tente de novo.')
        else:
            break
print('-='* 30)
print('{:<5}{:<13}{:<20}{}'.format('Cod.', 'Nome', 'Gols', 'Total'))
print('-'* 44)
for cod, jog in enumerate(time):
    print('{:^5}{:<13}{:<20}{}'.format(cod, jog['nome'], str(jog['gols']), sum(jog['gols'])))
print('-'* 44)
mostrar = 0
while mostrar != 999:
    while True: 
        mostrar = int(input('Mostrar dados de qual jogador?(999 para parar) '))
        if mostrar >= len(time) and mostrar != 999:
            print('Erro! Esse jogador não existe')
        elif mostrar == 999:
            break
        else:
            break
    if mostrar == 999:
        break
    print(f'__LEVANTAMENTO DO JOGADOR {time[mostrar]["nome"].upper()}__')
    for n, g in enumerate(time[mostrar]['gols']):
        print(f'  --No {n+1}° jogo fez {g} gols.')
    print('-'* 44)
print('<<VOLTE SEMPRE>>')