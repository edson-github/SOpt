aa = 0
a = 1
fim = int(input('Digite um termo: '))
for _ in range (0, fim):
    s = (aa + a)
    print(s, end = ' → ')
    aa = a
    a = s
print()
for s in range(fim + 1):
    if s % 2 == 0:
        print(s, end=' → ')
     
#https://pt.stackoverflow.com/q/411542/101
