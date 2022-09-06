n1 = int(input('Insert a number:'))
n2 = int(input('Insert a number:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
print('The sum equals to {}. \n The product equals to {}. \n The division equals to {:.3f}.'.format(s, m, d,), end=' ')
print('{} powered to {} equals to {}'.format(n1, n2, e))
