import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.5)
musica_de_fundo = pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')

largura = 640
altura = 480
largura_obj = 20
altura_obj = 20

x_cobra = int(largura/2 - largura_obj/2)
y_cobra = int(altura/2 - altura_obj/2)

velocidade = 10
x_controle = velocidade
y_controle = 0

pontos = 0
fonte = pygame.font.SysFont('comic sans', 30, True, True)

x_maca = randint(40,600)
y_maca = randint(50,430)
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo só que mais legal')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela,(0,255,0),(XeY[0],XeY[1],20,20))


def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cabeca, lista_cobra, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura/2 - largura_obj/2)
    y_cobra = int(altura/2 - altura_obj/2)
    lista_cabeca = []
    lista_cobra = []
    x_maca = randint(40,600)
    y_maca = randint(50,430)
    morreu = False




while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = - velocidade
            if event.key == K_s:
                if y_controle == - velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
    
    x_cobra += x_controle
    y_cobra += y_controle
    
    '''
    if pygame.key.get_pressed()[K_LEFT]:
        x_cobra -= 20
    if pygame.key.get_pressed()[K_RIGHT]:
        x_cobra += 20
    if pygame.key.get_pressed()[K_DOWN]:
        y_cobra += 20
    if pygame.key.get_pressed()[K_UP]:
        y_cobra -= 20
    '''
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra, y_cobra, largura_obj, altura_obj))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        pontos += 1
        comprimento_inicial += 1
        barulho_colisao.play()

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial',20,True,True)
        mensagem = 'Fim de jogo! Aperta R para continuar...'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
                        barulho_colisao.play()


            ret_texto.center = (largura//2,altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()


    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    
    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()
