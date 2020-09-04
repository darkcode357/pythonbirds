class Pessoa:
    def __init__(self,*filhos,nome=None,idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def comprimentar(self):
        return f'olá{id(self)}'

if __name__ == '__main__':
    darkcode = Pessoa(nome="darkcode")
    print(id(darkcode))
    print(darkcode.nome)
    luiz = Pessoa(darkcode,nome="luiz")
    for filho in luiz.filhos:
        print(filho.nome)
    print(darkcode.__dict__)
    print(luiz.__dict__)