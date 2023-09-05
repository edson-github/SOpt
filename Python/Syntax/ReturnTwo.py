def soma(a, b):
    x = a + b
    y = 'qualquer coisa'
    return x if x > 5 else y

def soma(a, b):
    yield a + b
    yield 'qualquer coisa'

def soma(a, b):
    x = a + b
    y = 'qualquer coisa'
    return (x, y)
    
#https://pt.stackoverflow.com/q/331155/101
