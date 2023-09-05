def somadig(n):
    return 0 if n == 0 else (n % 10) + somadig(n // 10)

print(somadig(120))

#https://pt.stackoverflow.com/q/349093/101
