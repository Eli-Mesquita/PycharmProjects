'''valor = list()
for cont in range(0, 5):
    valor.append(int(input('Digite um valor: ')))
print(f'Os valores digitados foram {valor}')
print(f'O maior valor digitado foi {max(valor)} na posicão {valor.index(max(valor))}')
print(f'O menor valor digitado foi {min(valor)} na posição {valor.index(min(valor))}')'''

valor = list()
for cont in range(0, 5):
    valor.append(int(input('Digite um valor: ')))
s = 0
print(f'Os valores digitados foram {valor}')
print(f'O maior valor digitado foi {max(valor)} nas posições:', end=' ')
for cont, v in enumerate(valor):
    s += v
    if v == max(valor):
        print(f'{cont + 1}', end=' / ')
print(f'\nO menor valor digitado foi {min(valor)} nas posições:', end=' ')
for cont, v in enumerate(valor):
    if v == min(valor):
        print(f'{cont + 1 }', end=' / ')
print(f'\nA soma dos valores digitados é igual a {s}')
