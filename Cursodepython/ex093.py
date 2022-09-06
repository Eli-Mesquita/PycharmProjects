jogador = {"Nome": '', "gols": [], "Total": 0}
jogador["Nome"] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, partidas):
    jogador["gols"].append(int(input(f'Quantos gols na partida {c+1}?')))
    jogador["Total"] = sum(jogador["gols"])
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c, g in enumerate(jogador["gols"]):
    print(f'    => Número de gols da {c+1}ª partida: {g}.')
print(f'{jogador["Nome"]} fez um Total de {jogador["Total"]} gols.')