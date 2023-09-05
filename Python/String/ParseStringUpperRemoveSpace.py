frase = input("Escreva uma frase: ")
fraseNova = "".join(chr.upper() for chr in frase if chr != " ")
print(fraseNova)

#https://pt.stackoverflow.com/q/340130/101
