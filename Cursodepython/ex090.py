ficha = dict()
ficha["Nome"] = str(input('Nome: '))
ficha["Média"] = float(input('Média: '))
if ficha["Média"] >= 7:
    ficha["Situação"] = 'APROVADO'
elif 7 > ficha["Média"] >= 5:
    ficha["Situação"] = 'RECUPERAÇÃO'
else:
    ficha["Situação"] = 'REPROVADO'
print(ficha)
for k, v in ficha.items():
    print(f'{k}: {v}')

