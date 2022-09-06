'''lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posição {pos}')
                break
            pos += 1
print(lista)'''

lista = []
pos = 0
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n >= max(lista):
        lista.append(n)
    elif n <= min(lista):
        lista.insert(0, n)
    for pos, n in enumerate(lista):
        if min(lista) < n < max(lista):
            lista.insert(pos, n)
        pos = pos + 1
print(lista)
