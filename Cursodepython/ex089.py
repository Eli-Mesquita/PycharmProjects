lista = list()
boletim = list()
while True:
    nome = lista.append(str(input('Nome: ')))
    n1 = lista.append(float(input('Nota 1: ')))
    n2 = lista.append(float(input('Nota 2: ')))
    boletim.append(lista[:])
    lista.clear()
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont in 'N':
        break
print('-=' * 30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, c in enumerate(boletim):
    media = (c[1]+c[2])/2
    print(f'{i+1:<4}2'
          f'{c[0]:<10}{media:>8.1f}')
print('-' * 26)
while True:
    mostrar = int(input('Mostrar notas do aluno número: (999 para sair) '))
    if mostrar == 999:
        break
    for i, c in enumerate(boletim):
        if mostrar == i+1:
            print(f'A notas de {c[0]} são {c[1]} e {c[2]}.')







