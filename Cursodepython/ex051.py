t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(t, 10*r, r):
    print(c, end=" - ")
print(']')