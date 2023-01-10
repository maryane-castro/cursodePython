#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols
#feitos durante o campeonato.

jogador = dict()
gols = list()
jogador['nome'] = str(input('Qual o nome do jogador? '))
q_part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1, q_part + 1):
    gols.append(int(input(f'Quantos gols na {c}° partida? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-='* 30 , '\n' , jogador, '\n' + '-='* 30)
for a in jogador.items():
    print(f'O campo {a[0]} tem o valor {a[1]}')
print('-='* 30)
print(f'O jogador {jogador["nome"]} jogou {q_part} partidas.')
for x in range(0, q_part):
    print(f'    => Na partida {x}, fez {gols[x]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')