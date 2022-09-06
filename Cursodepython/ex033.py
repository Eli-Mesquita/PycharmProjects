n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))
# verificar o menor valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor valor digitado foi {menor}')
maior = n1
if n2 > n1 and n2 > n3:
# verificar o maior valor
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor digitado foi: {maior}')

