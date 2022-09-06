c = s = 0
while True:
    n = int(input('Insira um valor (ou digite 999 para parar):  '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} números inseridos é igual a {s}')
