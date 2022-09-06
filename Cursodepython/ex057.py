sex = str(input('Inform your gender [M/F]: ')).strip().upper()[0]
while sex not in 'MF':
    sex = str(input('Invalid answer! Please inform you gender [M/F]: ')).strip().upper()[0]
print('Information registered')
