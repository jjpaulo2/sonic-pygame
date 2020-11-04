import pathlib, pygame

class TelaDeInicio:
    
    def __init__(self, tela):
        self.fundo_path = str(pathlib.Path(__file__).parent.absolute()) + "/../../img/fundo-menu.jpg"
        self.musica_path = str(pathlib.Path(__file__).parent.absolute()) + "/../../audio/title.wav"
        self.tela = tela

        self.fonte = pygame.font.Font(str(pathlib.Path(__file__).parent.absolute()) + "/../../fonts/ARCADECLASSIC.TTF", 40)
        self.press_start = self.fonte.render(" PRESS   ENTER ", False, (255,255,255), (30,35,150))
        self.EVENTO_PISCAR = pygame.USEREVENT + 1

    def tocar_musica(self):
        pygame.mixer.music.load(self.musica_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

    def renderizar_fundo(self):
        fundo = pygame.image.load(self.fundo_path)
        self.tela.blit(fundo, (0,0))

    def renderizar_press_start(self):
        self.tela.blit(self.press_start, (280,520))
        self.press_start_aparecendo = True

    def rodar_cenario(self):
        self.renderizar_fundo()
        self.tocar_musica()
        self.rodando = True
    
        self.renderizar_press_start()
        pygame.time.set_timer(self.EVENTO_PISCAR, 500)

    def atualizar_eventos(self, evento, fase):
        if evento.type == self.EVENTO_PISCAR:
            if self.press_start_aparecendo:
                self.renderizar_fundo()
                self.press_start_aparecendo = False
            else:
                self.renderizar_press_start()
                self.press_start_aparecendo = True

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                pygame.mixer.music.fadeout(500)
                pygame.time.set_timer(self.EVENTO_PISCAR, 0)
                self.rodando = False
    
    def atualizar_cenario(self):
        pass
