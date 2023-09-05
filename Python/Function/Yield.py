def ler_dados():
    with open('CTE_ARBA.txt', 'r') as arq:
        yield from arq.readlines()

for linha in ler_dados():
    print(linha)
    
#https://pt.stackoverflow.com/q/533379/101
