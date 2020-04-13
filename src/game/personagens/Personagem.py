from animacao.Animacao import Animacao

class Personagem:

    skin: str
    animacao: Animacao

    def __init__(self, skin, animacao):
        self.skin = skin
        self.animacao = animacao