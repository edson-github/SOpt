n1 = int(input())
n2 = int(input())
count = sum(1 for c in range(n1, n2) if c % n1 == 0)
print(f'O numero {n1} tem {count} multiplos menores que {n2}.')

#https://pt.stackoverflow.com/q/449499/101
