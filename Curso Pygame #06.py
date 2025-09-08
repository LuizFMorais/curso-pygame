import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
largura_obj = 40
altura_obj = 50

x = largura/2 - largura_obj/2
y = altura/2 - altura_obj/2

pontos = 0
fonte = pygame.font.SysFont('comic sans', 30, True, True)

x_azul = randint(40,600)
y_azul = randint(50,430)
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo só que mais legal')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
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
    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x, y, largura_obj, altura_obj))
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50))
    
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40,600)
        y_azul = randint(50,430)
        pontos += 1

    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()