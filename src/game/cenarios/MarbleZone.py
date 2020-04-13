import pathlib, pygame

class MarbleZone:
    
    def __init__(self, tela):
        self.fundo_path = str(pathlib.Path(__file__).parent.absolute()) + "/../../img/cenarios/marble-zone.jpg"
        self.musica_path = str(pathlib.Path(__file__).parent.absolute()) + "/../../audio/marble-zone.wav"
        self.tela = tela

    def tocar_musica(self):
        pygame.mixer.music.fadeout(500)
        pygame.mixer.music.load(self.musica_path)
        pygame.mixer.music.play()

    def renderizar_fundo(self):
        fundo = pygame.image.load(self.fundo_path)
        self.tela.blit(fundo, [0,0])

    def rodar_cenario(self):
        self.renderizar_fundo()
        self.tocar_musica()