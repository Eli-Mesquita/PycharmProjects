media = 0
idadetotal = 0
older_man = 0
older_man_name = ''
for p in range(1, 5):
    print(f'----- {p}ª pessoa -----')
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    idadetotal += idade

media = idadetotal / 4
print(media)

