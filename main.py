from vpython import *
from time import *

# cria box e mostra no navegador 
# segurar com botao direito ou esquerdo ao lado da caixa e arrastar para ver todos os lados

floor = box(pos=vector(0,-5,0), length=10, width=10, height=.1) # piso
ceiling = box(pos=vector(0,5,0), length=10, width=10, height=.1) # teto
backwall = box(pos=vector(0,0,-5), length=10, width=.1, height=10) # parede traseira
leftwall = box(pos=vector(-5,0,0), length=.1, width=10, height=10) # parede esquerda
rightwall = box(pos=vector(5,0,0), length=.1, width=10, height=10) # parede direita

marble = sphere(radius=.75, color=color.purple)

while True:
    pass