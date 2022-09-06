dados = {}
lista = []
while True:
    dados["Nome"] = str(input('Nome: '))
    dados["Sexo"] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while dados["Sexo"] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados["Sexo"] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    dados["Idade"] = int(input('Idade: '))
    lista.append(dados.copy())
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        print('ERRO! Por favor, Responda apenas S ou N.')
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print('-=' * 30)
print(lista)
print('-=' * 30)
print(f'1. Número total de membros cadastados: {len(lista)} ')
idade_total = media = 0
for c, v in enumerate(lista):
    idade_total += lista[c]["Idade"]
    media = idade_total/len(lista)
print(f'2. A média de idade dos membros cadastrados é: {media:5.2f} anos')
print(f'3. As mulheres cadastradas são: ', end="")
for c, v in enumerate(lista):
    if lista[c]["Sexo"] == 'F':
        print(lista[c]["Nome"], end=', ')
print()
print('4. Lista de membros acima da média de idade:')
for c, p in enumerate(lista):
    if lista[c]["Idade"] > media:
        for k, v in p.items():
            print(f'    {k}: {v}', end="; ")
        print()
print('-=' * 30)
print('Listagem encerrada')
print('-=' * 30)
