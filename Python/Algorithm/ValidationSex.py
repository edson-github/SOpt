def getSex():
    while True:
        sex = input('Digite seu sexo:')
        if sex in ['M', 'F']:
            return sex

print(getSex())

#https://pt.stackoverflow.com/q/257173/101
