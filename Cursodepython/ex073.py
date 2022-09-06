times = 'Palmeiras', 'Corinthians', 'Fluminense', 'Atlético-MG', 'Athletico-PR', 'Flamengo', 'Inter', \
        'Red Bull Bragantino', 'Santos', 'São Paulo', 'Botafogo', 'Ceará', 'Coritiba', 'Goiás', 'América-MG',\
        'Avaí', 'Cuiabá', 'Atlético-GO', 'Juventude', 'Fortaleza'
print('-=-'*15)
print(f"{'Brasileirão 2022' : ^40}")
print('-=-'*15)
print(f'Lista de times: {sorted(times)}')
print('-=-'*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=-'*15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=-'*15)
print(f"O Fortaleza está na {times.index('Fortaleza')+1}ª posição\n"
      f"O Ceará está na {times.index('Ceará')+1}ª posição")
print('-=-'*15)





