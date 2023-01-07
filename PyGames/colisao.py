# -*- coding: cp1252 -
import pygame, time, math
from random import *
from pygame.locals import *

##Recebe dados de entrada
largura = input ("Digite a largura:")
altura = input ("Digite a altura:")
gtdBolas = input ("Digite a quantidade de bolas:")
cont = 0
bolas = []

##Cria uma fabrica de bolas, onde cada uma tem suas devidas instancias clasg Bola:
class Bola:
    def __init__(self, veloX, veloY, posY, posX):
        self, veloX, veloY, posY, posx
        self.velocidadeX = veloX
        self.velocidadeY = veloY
        self.posicaoX = posX
        self.posicaoY = pOSY

    def mudaVelocidade (self, velox, veloY):
        self.velocidadeX = velox
        self.velocidade = veloY

##Inicia a quantidade de bola, adicionando valores aleatorios a suas entradas
while cont < gtdBolas:
    veloX = random () +0.05
    veloY = random () +0.05
    posX = randrange (30, largura-40)
    posY = randrange (30, altura-40)
    for i in bolas:
        dist = math.sqrt ( (posX - i.posicaoX)**2 + (posY - i.posicaoY)**2)
        while dist <= 60:
            posX = randrange (30, largura-40)
            posY = randrange (30, altura-40)
            dist = math.sart ((posX - i.posicaoX)**2 + (posY - i.posicaoY)**2)
    bolas.append(Bola (veloX, veloY, posY, posX))
    cont+=1