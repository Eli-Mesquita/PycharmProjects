pessoas = {'Nome': 'Eli', "Sobrenome": 'Mesquita', "Idade": 36, 'Sexo': 'M'}
print(pessoas)
print(pessoas['Idade'])
print(pessoas['Nome'])
print(f'{pessoas["Nome"]} {pessoas["Sobrenome"]} tem {pessoas["Idade"]} anos de idade.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas["Sobrenome"]
pessoas['Nome'] = 'Vivi'
pessoas["Peso"] = 98.5
for k, v in pessoas.items():
    print(f'{k}: {v}')

brasil = []
estado1 = {"UF": 'Ceará', "Sigla": 'CE'}
estado2 = {"UF": 'Rio Grande do Norte', "Sigla": 'RN'}
brasil.append(estado1)
brasil.append(estado2)
print(estado2["Sigla"])
print(brasil[1]["UF"])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado["uf"] = str(input('Unidade federativa: '))
    estado["sigla"] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f'{v}', end=' - ')
    print()


