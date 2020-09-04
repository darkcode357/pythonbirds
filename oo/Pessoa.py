class Pessoa:
    def __init__(self,nome=None,idade=35):
        self.idade = idade
        self.nome = nome
    def comprimentar(self):
        return f'olá{id(self)}'

if __name__ == '__main__':
    p = Pessoa("darkcode")
    print(id(p))
    print(p.nome)