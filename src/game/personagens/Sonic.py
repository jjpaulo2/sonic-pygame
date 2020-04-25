from pygame.sprite import Sprite, Group
import pygame, pathlib

def carregar_imagem(nome):
    return pygame.image.load(str(pathlib.Path(__file__).parent.absolute()) + "/../../img/sonic/" + nome)

class SonicSprite(Sprite):

    def __init__(self, x=100, y=350):

        super(SonicSprite, self).__init__()

        self.velocidade_x = 0
        self.velocidade_y = 0
        self.x = x
        self.y = y

        self.images = []
        self.images.append(carregar_imagem("sonic-correndo-esquerda-3.png"))
        self.images.append(carregar_imagem("sonic-correndo-esquerda-2.png"))
        self.images.append(carregar_imagem("sonic-correndo-esquerda-1.png"))
        self.images.append(carregar_imagem("sonic-stop-esquerda.png"))
        self.images.append(carregar_imagem("sonic-stop.png"))
        self.images.append(carregar_imagem("sonic-correndo-direita-3.png"))
        self.images.append(carregar_imagem("sonic-correndo-direita-1.png"))
        self.images.append(carregar_imagem("sonic-correndo-direita-2.png"))

        self.index = 4
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.y , 100, 107)

    def update(self):
        self.rect.move_ip(self.velocidade_x, self.velocidade_y)
        print("velocidade_x = %d"%self.velocidade_x)

        if self.velocidade_x > 0:
            self.index += 1
            if self.index >= 8:
                self.index = 4
        elif self.velocidade_x < 0:
            self.index -= 1
            if self.index <= -1:
                self.index = 3

        self.image = self.images[self.index]

    def stop(self):
        if self.velocidade_x > 0:
            self.index = 4
        elif self.velocidade_x < 0:
            self.index = 3
        self.velocidade_x = 0
        self.update()
