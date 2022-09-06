'''n = input('Insira um número entre 0 e 9999: ')
print('unidade:',(n[:3]))
print('dezena:',n[2:3])
print('centena:',n[0:1:1])
print('milhar: {}'.format(n[0:1]))'''

'''n = input('Digite um número entre 0 e 9999: ')
add = '000' + n
print(add)
print(f'unidade: {add[-1]}')
print(f'dezena: {add[-2]}')
print(f'centena: {add[-3]}')
print(f'milhar: {add[-4]}')'''

n = int(input('Digite um número entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena : {c}')
print(f'Milhar: {m}')

