n = input('Type anything here:')
print('The primitive type of this value is:', (type(n)))
print('is it space only?', n.isspace())
print('Is it a number?', n.isnumeric())
print('Is it alphabetic?', n.isalpha())
print('Is it alphanumeric?', n.isalnum())
print('Is it all caps?', n.isupper())
print('Is it all lowercase?', n.islower())
print('Is it capitalized?', n.istitle())