def somentenumeros(entrada):
    try:
        int(entrada)
        return True
    except:
        return False

while True:
    cpf = input('Digite seu CPF ou digite os nove primeiros digitos ')
    if somentenumeros(cpf) and len(cpf) in {9, 11}:
        break
    else:
        print('Erro. O valor digitado era inválido.')
print(cpf)

#http://pt.stackoverflow.com/q/187869/101
