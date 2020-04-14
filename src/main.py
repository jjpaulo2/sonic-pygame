#!/bin/python3

import pygame, configparser, pathlib

from game.cenarios.GreenHillZone import GreenHillZone
from game.cenarios.MarbleZone import MarbleZone
from game.telas.TelaDeInicio import TelaDeInicio

pygame.mixer.pre_init(44100, 16, 2, 1024)
pygame.init()

config = configparser.ConfigParser()
config.read("config.ini")
JANELA = [int(config['JANELA']['LARGURA']), int(config['JANELA']['ALTURA'])]

tela = pygame.display.set_mode(JANELA)
pygame.display.set_caption("Sonic Pygame")
clock = pygame.time.Clock()

#inicio = TelaDeInicio(tela)
#inicio.rodar_cenario()

fase1 = GreenHillZone(tela)
fase1.rodar_cenario()
fase = 1
#fase2 = MarbleZone(tela)

executando = True
while executando:
    for evento in pygame.event.get():

        if fase == 1: 
            fase1.atualizar_cenario(evento)

        if evento.type == pygame.QUIT:
            executando = False

    clock.tick(30)
    pygame.display.update()
    pygame.display.flip()

pygame.quit()