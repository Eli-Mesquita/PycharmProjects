exp = str(input('Insira uma expressão: '))
check = []
for par in check:
    if par == '(':
        check.append('(')
    elif par == ')':
        if len(check) > 0:
            check.pop()
        else:
            check.append(')')
            break
if len(check) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está incorreta.')

