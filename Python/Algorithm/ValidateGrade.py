import sys

n1 = int(input('digite nota 1: '))
n2 = int(input('digite nota 2: '))
if n1 > 10:
    print(f'{n1} não é uma nota válida!')
    sys.exit(0)
if n2 > 10:
    print(f'{n2} não é uma nota válida!')
    sys.exit(0)
media = (n1 + n2) / 2
if media >= 7:
    print(f'Você foi aprovado com média {media}')
else:
    print(f'Você foi reprovado com média {media}')
    
#https://pt.stackoverflow.com/q/446515/101
