termo = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razão? '))
t = termo
cont = 1
total = 0
nt = 10
while nt != 0:
    total += nt
    while cont <= total:
        print(t, end=' - ')
        t += r
        cont += 1
    print('Pausa')
    nt = int(input('Quantos termos quer mostrar? '))
print(f'Progressão finalizada com um total de {total} termos apresentados.')


