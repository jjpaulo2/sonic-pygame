import pathlib, pygame

from ..personagens.Sonic import *

class GreenHillZone:
    
    def __init__(self, tela):
        self.fundo_path = str(pathlib.Path(__file__).parent.absolute()) + "/../../img/cenarios/green-hills.png"
        self.musica_path = str(pathlib.Path(__file__).parent.absolute()) + "/../../audio/green-hill-zone.wav"
        self.tela = tela

        self.sonic = SonicSprite()
        self.grupo_sprites = pygame.sprite.Group(self.sonic)

    def tocar_musica(self):
        pygame.mixer.music.load(self.musica_path)
        pygame.mixer.music.play()

    def renderizar_fundo(self):
        fundo = pygame.image.load(self.fundo_path)
        self.tela.blit(fundo, [0,0])

    def rodar_cenario(self):
        self.renderizar_fundo()
        self.tocar_musica()

        self.rodando = True
        
    def atualizar_cenario(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                self.sonic.velocidade_x = 10
            if evento.key == pygame.K_LEFT:
                self.sonic.velocidade_x = -10

        if evento.type == pygame.KEYUP:
            self.sonic.stop()

        if self.sonic.rect[0] > self.tela.get_rect()[2] :
            pygame.mixer.music.fadeout(500)
            self.rodando = False


        self.renderizar_fundo()
        self.grupo_sprites.update()
        self.grupo_sprites.draw(self.tela)

        
