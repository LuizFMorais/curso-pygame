import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('bunana_espera/bunana_espera0.png'))
        self.sprites.append(pygame.image.load('bunana_espera/bunana_espera1.png'))
        self.sprites.append(pygame.image.load('bunana_espera/bunana_espera2.png'))
        self.sprites.append(pygame.image.load('bunana_espera/bunana_espera3.png'))
        self.sprites.append(pygame.image.load('bunana_espera/bunana_espera4.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (12*9, 18*9))

        self.rect = self.image.get_rect()
        self.rect.topleft = 300, 300

    def update(self):
            self.atual = self.atual + 0.2
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (12*9, 18*9))

todas_as_sprites = pygame.sprite.Group()
personagem = Personagem()
todas_as_sprites.add(personagem)

imagem_fundo = pygame.image.load('praia_fundo.png').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo,(largura,altura))

PRETO = (255,255,255)

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(PRETO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    tela.blit(imagem_fundo, (0,0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()