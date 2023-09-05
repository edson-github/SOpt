import random

ConvInicial = str(input('Você: '))
if ConvInicial in {
    'Não estou passando bem',
    'Estou com dor',
    'Preciso de ajuda',
}:
    while True:
        print('O que você está sentindo?')
        RespDor = input('Você: ')
        if RespDor in [
            'Estou com dor de cabeça',
            'Dor de cabeça',
            'Minha cabeça dói',
        ]:
            print(
                f"Você pode usar um {random.choice(['Neosaldina', 'Dorflex', 'Advil', 'Tylenol', 'Aspirina', 'Naldecon'])} para aliviar sua dor!"
            )
            break; #para encerrar o laço de repetição
        else:
            print('Não entendi, poderia ser mais claro?')
            
#https://pt.stackoverflow.com/q/336185/101
