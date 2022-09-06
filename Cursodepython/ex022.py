nome = str(input('Informe o seu nome completo: '))
print(f'Em maiúsculas:',nome.upper())
print('Em minúsculas: ',nome.lower())
#print('Seu nome completo tem um total de {} letras.'.format(len(nome.replace(' ', ''))))
print('Seu nome completo tem um total de {} letras.'.format(len(nome) - (nome.count(' '))))
#first = (nome.split())
#print('Seu primeiro nome tem um total de {} letras.'.format(len(first[0])))
print('Seu primeiro nome tem um total de {} letras.'.format(nome.find(' ')))

