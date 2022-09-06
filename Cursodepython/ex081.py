lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SsNn':
        cont = str(input('Continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
lista.sort(reverse=True)
print('-=-'*20)
print(f'Você digitou {len(lista)} elementos')
print(f'A ordem decrescente dos valores é: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')


