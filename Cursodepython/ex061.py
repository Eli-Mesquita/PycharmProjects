termo = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razão? '))
t = termo
cont = 1
while cont <= 10:
    print(t, end=' - ')
    t += r
    cont += 1
print('FIM')



