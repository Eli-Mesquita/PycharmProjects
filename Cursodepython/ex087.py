matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = maior = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número na posição {l, c}: '))
print('-='*10)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
    print()
print(f'A soma dos números pares é igual a: {somap}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos números da terceira coluna é igual a: {scol}')
for c in range(0, 3):
    if matriz[1][c] > 0 and matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número da segunda linha é: {maior}')



