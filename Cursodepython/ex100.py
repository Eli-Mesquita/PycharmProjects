from random import sample
from time import sleep

def sorteio():
    print('Sorteando 6 valores da lista: ', end='')
    lista.append(sample(range(1, 60), 6))
    for v in lista:
        sleep(0.5)
        print(sorted(v), flush=True, end=' ')
    print()

def somapar():
    for i, v in enumerate(lista):
            print(v)


lista = []
sorteio()
somapar()
