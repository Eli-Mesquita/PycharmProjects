time = list()
partidas = list()
jogador = dict()
while True:
    jogador.clear()
    jogador["Nome"] = str(input('Nome: '))
    n = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, n):
        partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
    jogador["gols"] = partidas[:]
    jogador["Total"] = sum(partidas)
    time.append(jogador.copy())
    cont = str(input('Deseja continuar? ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar? ')).upper().strip()[0]
    if cont == 'N':
        break
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('-' * 40)