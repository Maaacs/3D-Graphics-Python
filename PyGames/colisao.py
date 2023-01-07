# -*- coding: cp1252 -
import pygame, time, math
from random import *
from pygame.locals import *

##Recebe dados de entrada
largura = input ("Digite a largura:")
altura = input ("Digite a altura:")
qtdBolas = input ("Digite a quantidade de bolas:")
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
while cont < qtdBolas:
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

#inicia a quantidade de bola, adicionando valores aleatorios a suas entradas 
while cont < qtdBolas:
    veloX = random () +0.05
    veloY = random () +0.05
    posX = randrange (30, largura-40)
    posY = randrange (30, altura-40)
    for i in bolas:
        dist = math.sqrt((posX - i.posicaoX)**2 + (posY - i.posicaoy) **2)
        while dist <= 60:
            posX = randrange (30, largura-40)
            posY = randrange (30, altura-40)
            dist = math.sgrt ((posX - i.posicaoX)**2 + (posY - i.posicaoY)**2)
    bolas.append (Bola (veloX, veloY, posY, posX))
    cont+= 1

parou = 0
pygame.init () ##Inicia os módulos do PYGAME
window = pygame.display.set_mode((largura, altura)) ##Cria uma tela.. X e Y
pygame.display.set_caption ("Colisao")##Nomeia a Janela
tela = pygame.display.get_surface () ##)
bola = pygame.image.load('bola.png').convert_alpha()
bolaBranca = pygame.image.load ('bolaBranca.png').convert_alpha()
pygame.display.set_icon(bola) #Coloca o icone
cor_branca = (255,255, 255)
window.fill (cor_branca)
pygame.display.flip()
pygame.display.update()
