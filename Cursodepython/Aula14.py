'''for c in range(1, 11):
    print(c)'''
import random

'''a = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    a += n
print(a/3)'''


'''c = 0
while c < 11:
    print(c)
    c = c + 1'''
'''n = 0
cpu = random.randint(0, 5)
while n != cpu:
    n = int(input('Digite um número entre 0 e 5:'))
print('Você acertou!')'''

'''r = 'S'
while r == 'S':
    p = input('Qual o seu nome?: ').upper()
    r = input('Quer continuar? [S/N] ').upper()
print(f'Tá, {p}, Não precisa gritar! \n'
      f'ninguém tem paciência comigo')'''

n = 1
even = odd = 0
while n != 0:
    n = int(input('Insert a number: '))
    if n != 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
print(f'You typed {even} even numbers and {odd} odd numbers.')



