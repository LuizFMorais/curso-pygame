import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
largura_obj = 40
altura_obj = 50
x = largura/2 - largura_obj/2
y = altura/2 - altura_obj/2

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo só que mais legal')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_LEFT]:
        x -= 20
    if pygame.key.get_pressed()[K_RIGHT]:
        x += 20
    if pygame.key.get_pressed()[K_DOWN]:
        y += 20
    if pygame.key.get_pressed()[K_UP]:
        y -= 20
    pygame.draw.rect(tela, (255,0,0), (x, y, largura_obj, altura_obj))
    
    pygame.display.update()
