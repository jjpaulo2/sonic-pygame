#!/bin/python3

import pygame, configparser, pathlib

from game.cenarios.GreenHillZone import GreenHillZone
from game.cenarios.MarbleZone import MarbleZone
from game.telas.TelaDeInicio import TelaDeInicio

pygame.mixer.pre_init(44100, 16, 2, 1024)
pygame.init()

config = configparser.ConfigParser()
config.read("src/config.ini")
JANELA = [int(config['JANELA']['LARGURA']), int(config['JANELA']['ALTURA'])]

tela = pygame.display.set_mode(JANELA)
pygame.display.set_caption("Sonic Pygame")
pygame.key.set_repeat(10,10)
clock = pygame.time.Clock()

inicio = TelaDeInicio(tela)
inicio.rodar_cenario()

fase1 = GreenHillZone(tela)
fase2 = MarbleZone(tela)
fase = 0

executando = True
while executando:
    for evento in pygame.event.get():

        if fase == 0:
            inicio.atualizar_cenario(evento, fase)
            if not inicio.rodando: 
                fase += 1
                fase1.rodar_cenario()
        elif fase == 1: 
            fase1.atualizar_cenario(evento)
            if not fase1.rodando: 
                fase += 1
                fase2.rodar_cenario()
        elif fase == 2:
            fase2.atualizar_cenario(evento)

        if evento.type == pygame.QUIT:
            executando = False

    clock.tick(30)
    pygame.display.flip()

pygame.quit()