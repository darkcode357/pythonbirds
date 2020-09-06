class Motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        self.velocidade+1
    def frear(self):
        self.velocidade-=2
        self.velocidade=max(0,self.velocidade)
NORTE='Norte'
SUL='Sul'
LEST='Lest'
OEST='Oest'

class Direcao:
    rotacao_a_direita_dct={NORTE:LEST,LEST:SUL,SUL:OEST,OEST:NORTE}
    rotacao_a_direita_dct={NORTE:OEST,LEST:NORTE,SUL:LEST,OEST:SUL}
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor=self.rotacao_a_direita_dct[self.valor]
    def girar_a_esquerda(self):
        self.valor=self.rotacao_a_direita_dct[self.valor]