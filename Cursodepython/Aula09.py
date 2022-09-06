'''
Fatiamento de String
frase[0:]
Análise:
    len()
    count()
    find()
    in
Transformação:
    replace()
    upper()
    lower()
    capitalize()
    title()
    strip()
    rtrip()
    lstrip()
Divisão: split()
Junção: =join() '''

frase = 'Curso em Vídeo Python'
print(frase[0:21])
print(frase[15:])
print(len(frase))
print(frase.count('o'))
print(frase.find('Android'))
print('video' in frase)
print(frase.replace('Python' , 'Android'))
print(frase.replace('Curso', 'Aula'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase = '   Aprenda Python  '
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
frase = 'Curso em Vídeo Python'
print(frase.split())
print('-'.join(frase))

frase = """Olá, eu sou o Eli e estou aprendendo Python através do canal
Curso em video. Estou tendo uma otima experiencia e queria externar minha
gratidão a todos que colaboraram para a existência desse curso e sua
disponibilidade gratuita no YouTube."""
print(frase)
print(len(frase))
print(frase.find('YouTube'))
print(frase.count('ou'))
nw = input('Digite a nova palavra:')
print(frase.replace('Python', nw.upper()))
print('curso' in frase)
import math
rand = (frase.split())
print(rand [0])





