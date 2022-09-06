termo = int(input('Quantos termos quer mostrar '))
t = termo
f1 = 0
f2 = 1
total = 3
print(f'{f1} - {f2} -', end= ' ')
nt = t + 3
while nt != 0:
    nt += nt
    while total <= t:
        fn = f1 + f2
        print(fn, end=' - ')
        f1 = f2
        f2 = fn
        total += 1
    print('Pausa')
    nt = int(input('Quantos termos quer mostrar a mais? '))
print('Sequência finalizada')