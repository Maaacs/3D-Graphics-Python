from vpython import *
from time import *

# cria box e mostra no navegador 
# segurar com botao direito ou esquerdo ao lado da caixa e arrastar para ver todos os lados

floor = box(pos=vector(0,-5,0), size=vector(10, .1, 10)) # piso # length, width, height
ceiling = box(pos=vector(0,5,0), size=vector(10, .1, 10))  # teto
backwall = box(pos=vector(0,0,-5), size=vector(10, 10, .1))  # parede traseira
leftwall = box(pos=vector(-5,0,0), size=vector(.1,10, 10))  # parede esquerda
rightwall = box(pos=vector(5,0,0), size=vector(.1, 10, 10))  # parede direita

marble = sphere(radius=.75, color=color.purple)

deltaX=.1
xPos=0

while True:
    # movimento para bola
    rate(10)
    xPos=xPos+deltaX
    if (xPos>4 or xPos<-4): # evita passar direto pela parede
        deltaX=deltaX*(-1)
    marble.pos=vector(xPos,0,0)