def media(*lista):
    soma = sum(lista)
    return soma // len(lista)
lista = [7, 8, 9]
print(media(*lista))

#https://pt.stackoverflow.com/q/361203/101
