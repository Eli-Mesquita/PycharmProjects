'''lista = list()
par = list()
impar = list()
for c in range(0,7):
    lista.append(int(input(f'Digite o {c +1}º número: ')))
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(F'os números pares foram: {par}')
print(F'os números ímpares foram: {impar}')'''

lista = [[], []]
n = 0
for c in range(1,8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os números pares foram {lista[0]}')
print(f'Os números impares foram {lista[1]}')
print(lista)


