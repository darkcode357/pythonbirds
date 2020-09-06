class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'olá{id(self)}'

    @staticmethod
    def metodo_estatico():
        return 10
    @classmethod
    def nome_e_atributos_de_class(cls):
        return f'{cls}-olhos{cls.olhos}'

if __name__ == '__main__':
    darkcode = Pessoa(nome="darkcode")
    print(id(darkcode))
    print(darkcode.nome)
    luiz = Pessoa(darkcode, nome="luiz")
    for filho in luiz.filhos:
        print(filho.nome)
    darkcode.olhos = 12
    print(darkcode.__dict__)
    print(luiz.__dict__)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos), id(darkcode.olhos), id(luiz.olhos))
    print(Pessoa.metodo_estatico())
    print(darkcode.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_class())
    print(darkcode.nome_e_atributos_de_class())