'''dados = list()
dados.append('Eli')
dados.append(36)
nomes = list()
nomes.append(dados[:])
dados[0] = 'Maria'
dados[1] = '22'
nomes.append(dados[:])
print(nomes)'''

'''family = [['Eli', 36], ['Vitória', 23], ['Sasha', 3]]
#print(family[2][0])
for p in family:
    print(f'{p[0]} tem {p[1]} anos de idade')
    #print(p[0], '-', p[1])'''

family = list()
dados = list()
maior = menor = 0
for info in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    family.append(dados[:])
    dados.clear()
for p in family:
    #print(f'{p[0]} tem {p[1]} anos de idade')
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores.')