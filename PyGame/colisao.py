#créditos: Luan Klein
import pygame, time, math
from random import *
from pygame.locals import *

##Recebe dados de entrada
largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))
qtdBolas = int(input("Digite a quantidade de bolas:"))
cont = 0
bolas = []

##Cria uma fabrica de bolas, onde cada uma tem suas devidas instancias clasg Bola:
class Bola:
    def __init__(self, veloX, veloY, posY, posX):
        self, veloX, veloY, posY, posX
        self.velocidadeX = veloX
        self.velocidadeY = veloY
        self.posicaoX = posX
        self.posicaoY = posY

    def mudaVelocidade (self, velox, veloY):
        self.velocidadeX = velox
        self.velocidade = veloY

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

# Funçao calculadora de velocidades apos as colisões
def calculaVelocidade (vx1, vy1, vx2, vy2, p1, p2):
    projVx1 = (float ((p1*vx1 + p2*vy1)) / float((p1**2+p2**2))) * p1 ##Projeção da velocidade X da bola 1 em relação ao Eixo
    projVy1 = (float ((p1*vx1 + p2*vy1)) / float((p1**2+p2**2))) * p2
    
    projVx2 = (float((p1*vx2 + p2*vy2)) / float((p1**2+p2**2))) * p1
    projVy2 = (float((p1<vx2 + p2*vy2)) / float((p1**2+p2**2))) * p2
    
    vx1f = vx1 - projVx1 + projVx2 # Velocidade Inicial
    vy1f = vy1 - projVy1 + projVy2 # velocidade da projeção + velocidade projeção 2
    
    vx2f = vx2 - projVx2 + projVx1
    vy2f =  vy2 - projVy2 + projVy1

    return vx1f, vy1f, vx2f, vy2f

while True:
    ##pygame .time .wait (1)
    cont = 0
    while cont < qtdBolas:
        ##Veriffica se as bolas colidiram na parede
        if bolas[cont].posicaoX+50 >= largura or bolas[cont].posicaoX <= 0:
            bolas[cont].velocidadeX *= -1
        
        if bolas[cont].posicaoY+50 >= altura or bolas[cont].posicaoY <= 0:
            bolas[cont].velocidadeY *= -1
        i = cont + 1

        while i < qtdBolas:
            ##verifica se as bolas colidiram entre si
            dist = math.sqrt((bolas[cont].posicaoX - bolas[i].posicaoX)**2 + (bolas[cont].posicaoY - bolas[i].posicaoY) **2)
            if dist <= 50:
                ##Se sim, chama a função para verificar as novas velocidades
                p1 = bolas[cont].posicaoX - bolas[i].posicaoX
                p2 = bolas[cont].posicaoY - bolas[i].posicaoY

                vx1, vy1, vx2, vy2 = calculaVelocidade(bolas[cont].velocidadeX, bolas[cont].velocidadeY, bolas[i].velocidadeX, bolas[i].velocidadeY,p1,p2)
                ##Chama os métodos implementados na classe bola para fazer mudanca de variavel
                bolas[cont].mudaVelocidade(vx1, vy1)
                bolas[i].mudaVelocidade (vx2, vy2)
            i+= 1
        cont+= 1
    
    ##Faz as bolinhas se mexerem
    for i in bolas:
        ##some com as bolinhas na posição velha
        tela.blit(bolaBranca, (i.posicaoX, i.posicaoY))
        i.posicaoX += i.velocidadeX
        i.posicaoY += i.velocidadeY
        ##Coloca ela na posição nova
        tela.blit(bola, (i.posicaoX, i.posicaoY))
    
    pygame.display.flip()
    pygame.display.update()
    for event in pygame.event.get() :
        ## Verifica se o usuario apertou a tecla Q
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit() ## Fecha a tela do pygame
                parou = 1
        if event.type == pygame.QUIT: ## Verifica se o usuario clicou no X vermelho para fechar
            pygame.quit()
            parou = 1
    if parou == 1:
        break 
