#!/bin/python3

import pygame, configparser, pathlib

from .game.cenarios.GreenHillZone import GreenHillZone
from .game.cenarios.MarbleZone import MarbleZone
from .game.telas.TelaDeInicio import TelaDeInicio

pygame.mixer.pre_init(44100, 16, 2, 1024)
pygame.init()

config = configparser.ConfigParser()
config.read("sonic/config.ini")
JANELA = [int(config['JANELA']['LARGURA']), int(config['JANELA']['ALTURA'])]

tela = pygame.display.set_mode(JANELA)
pygame.display.set_caption("Sonic Pygame")
clock = pygame.time.Clock()

fase_object = [
    TelaDeInicio(tela),
    GreenHillZone(tela),
    MarbleZone(tela)
]
fase = 0
fase_object[fase].rodar_cenario()

executando = True
while executando:

    fase_object[fase].atualizar_cenario()

    for evento in pygame.event.get():

        if fase == 0:
            fase_object[fase].atualizar_eventos(evento, fase)
        else: 
            fase_object[fase].atualizar_eventos(evento)
            fase_object[fase].sonic.update()

        if not fase_object[fase].rodando: 
            fase += 1
            fase_object[fase].rodar_cenario()

        if evento.type == pygame.QUIT:
            executando = False

    clock.tick(30)
    pygame.display.flip()

pygame.quit()