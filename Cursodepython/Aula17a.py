'''num = [2, 5, 9, 1]
num[0] = 3
num.append(7)
num.insert(2, 5)
print(num)
num.sort(reverse=True)
print(num)
print(f'Número de elementos: {len(num)}')
#num.pop(1)
if 8 in num:
    num.remove(8)
else:
    print('Esse valor não está na lista')
print(num)'''

'''valor = []
valor.append('pitu')
valor.insert(0,1)
valor.append(9)
valor.insert(1, 5)'''

'''valor = list()
for cont in range(0, 5):
    valor.append(int(input('Digite um Valor: ')))
s = 0
for c, v in enumerate(valor):
    print(f'Na posição {c +1} está o valor {v}...')
    s += v
print(s)
print('fim')'''

a = [1, 2, 3, 4, 5]
b = a[:]
b[0] = 0
print(a, b)
print(a + b)

