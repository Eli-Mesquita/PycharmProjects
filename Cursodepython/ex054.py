from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 7):
    birth = int(input(f'Qual o ano de nascimento da {c}ª pessoa? '))
    age = ano - birth
    if age >= 18:
        maior += 1
    else:
        menor += 1
print(f' Ao todo tivemos {maior} pessoas maiores de idade ')
print(f'E tivemos {menor} menores de idade.')
