lista = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    cont = input('Quer continuar? [S/N] ').upper().strip()[0]
    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ').upper().strip()[0]
    if cont == 'N':
        print('-=' * 20)
        print('Cadastro Finalizado!')
        print('-=' * 20)
        break
print(f'Você cadastrou {len(lista)} pessoas.')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'tem o maior peso com {maior} Kg.')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print(f'tem o menor peso com {menor} Kg.')
