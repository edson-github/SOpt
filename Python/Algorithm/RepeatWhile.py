while True:
    sex = input('Digite seu sexo:')
    if sex in ['M', 'F']:
        break

sex = input('Digite seu sexo:')
while sex not in ['M', 'F']:
    sex = input('Digite seu sexo:')
    
#https://pt.stackoverflow.com/q/257156/101
