s = 0
c = 0
for n in range(1,500):
    if n % 2 == 1:
        if n % 3 == 0:
            s += n
            c = c + 1
print(f'A soma dos {c} valores é igual a {s}')
