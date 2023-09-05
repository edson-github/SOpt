n = int(input("Digite o termo da sequência Fibonacci: "))
a = 1
b = 1
k = 1
while k <= n - 2:
    tmp = a
    a = b
    b = tmp + b
    k += 1
print(f"O {n}º da Sequência de Fibonacci é ocupado pelo número {b}.")

#https://pt.stackoverflow.com/q/358586/101
