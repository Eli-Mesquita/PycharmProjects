frase = str(input('Digite uma frase: ')).strip()
analise = ' ' + frase
print('A letra A aparece {} vezes na frase.'.format(analise.lower().count('a')))
print('A primeira letra A aparece na posição {}.'.format(analise.lower().find('a')))
print('A última letra A aparece na posição {}.'.format(analise.lower().rfind('a')))

