
phrase = str(input('Insert a sentence: ')).strip().upper()
word = phrase.split()
join = ''.join(word)
invert = join [::-1]
'''for letter in range(len(join) -1, -1, -1):
    invert += join[letter]'''
print(f'A frase {phrase} ao inverso é {invert}.')
if join == invert:
    print('PALÍNDROMO')
else:
    print('Não é um PALÍNDROMO')
