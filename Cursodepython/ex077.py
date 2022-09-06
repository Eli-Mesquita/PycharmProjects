lista = ('aprender','programar', 'linguagem', 'estudar')
for p in lista:
    print(f'\nNa palavra {p.upper()} temos as vogais:', end= ' ')
    for vogais in p:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')





