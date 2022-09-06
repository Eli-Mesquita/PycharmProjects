matriz = [[0, 0], [0, 1], [0, 2],
          [1, 0], [1, 1], [1, 2],
          [2, 0], [2, 1], [2, 2]]
n = 0
for p in matriz:
    n = int(input(f'Insira um número na posição {p}: '))
    p.clear()
    p.append(n)
print(f'{matriz[0]} | {matriz[1]} | {matriz[2]}\n'
      f'{matriz[3]} | {matriz[4]} | {matriz[5]}\n'
      f'{matriz[6]} | {matriz[7]} | {matriz[8]}')
print(n)




