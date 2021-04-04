#!/bin/python3

import pygame,configparser,pathlib

import PySimpleGUI as PythonGUI

from game.cenarios.GreenHillZone import GreenHillZone
from game.cenarios.MarbleZone import MarbleZone
from game.cenarios.ChemicalPlantZone import ChemicalPlantZone
from game.cenarios.StarLightZone import StarLightZone
from game.cenarios.DoomsdayZone import DoomsdayZone
from game.telas.TelaDeInicio import TelaDeInicio




# layout = [[PythonGUI.Text('Type something on Python GUI Input. Then, Python GUI Input will recognize it.')],
                 # [PythonGUI.InputText()],
                 # [PythonGUI.Submit(), PythonGUI.Cancel()]]

# window = PythonGUI.Window('Python GUI Input', layout)

# event, values = window.read()
# window.close()

# text_input = values[0]
# PythonGUI.popup('You typed', text_input, 'on Python GUI Input.')



pygame.mixer.pre_init(44100, 16, 2, 1024)
pygame.init()

config = configparser.ConfigParser()
config.read("sonic/config.ini")
JANELA = [int(config['JANELA']['LARGURA']), int(config['JANELA']['ALTURA'])]

tela = pygame.display.set_mode(JANELA)
pygame.display.set_caption("Sonic the Hedgehog Demo")
clock = pygame.time.Clock()

fase_object = [
    TelaDeInicio(tela),
    GreenHillZone(tela),
    MarbleZone(tela),
    StarLightZone(tela),
    ChemicalPlantZone(tela),
    DoomsdayZone(tela)   
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

        if  fase_object[fase].rodando == 1: 
            fase += 1
            if not fase == 0:
                fase_object[fase].sonic.rect[0]=30;
            fase_object[fase].rodar_cenario()
            
        if  fase_object[fase].rodando == 2: 
            fase -= 1
            if not fase == 0:
                fase_object[fase].sonic.rect[0]=770;
            fase_object[fase].rodar_cenario() 
            
        if  fase_object[fase].rodando == 3: 
            executando = False

        if evento.type == pygame.QUIT:
            executando = False
            # for i in range(0,1000):
                # PythonGUI.one_line_progress_meter('Sonic the Hedgehog Demo', i+1, 1000, 'key','Please wait...')
            for i in range(0,1000):
                PythonGUI.one_line_progress_meter('Sonic the Hedgehog Demo', i+1, 1000, 'key','Demo closing...')
            

    clock.tick(30)
    pygame.display.flip()

pygame.quit()


# layout = [[PythonGUI.Text('Type something on Python GUI Input. Then, Python GUI Input will recognize it.')],
                 # [PythonGUI.InputText()],
                 # [PythonGUI.Submit(), PythonGUI.Cancel()]]

# window = PythonGUI.Window('Thanks for playing!', layout)

# event, values = window.read()
# window.close()

# text_input = values[0]


PythonGUI.popup('Goodbye!')