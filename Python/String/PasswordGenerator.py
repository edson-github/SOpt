from random import choice

minusculas = "abcdefgh"
maiusculas = "ABCDEFGH"
senha = []
for _ in range(8):
    senha.extend((choice(maiusculas), choice(minusculas)))
print(''.join(senha))

#https://pt.stackoverflow.com/q/461052/101
