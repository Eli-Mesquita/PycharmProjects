n = 1
s = 0
c = 0
while n != 0:
    n = int(input('Digite um número qualquer - [ 0 ] para parar: '))
    s += n
    c += 1
print('Finalizando...')
print(f'A soma dos {c -1} números inseridos foi: {s} ')