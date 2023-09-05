class People:
    nome = ""
    def __init__(self, nome):
        self.nome = nome
    def talk(self):
        print(f'Meu nome é {self.nome}')

p1 = People("joão")
p1.talk()

#https://pt.stackoverflow.com/q/514661/101
