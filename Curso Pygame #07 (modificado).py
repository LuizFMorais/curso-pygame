import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

menu = 0

pygame.mixer.music.set_volume(0.5)
musica_de_fundo = pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')

largura = 640
altura = 480
largura_obj = 40
altura_obj = 50
a = 0
opcao = 0

x = int(largura/2 - largura_obj/2)
y = int(altura/2 - altura_obj/2)

pontos = 0
tempo = 0
fonte = pygame.font.SysFont('comic sans', 30, True, False)
fonte2 = pygame.font.SysFont('impact', 50, False, False)

x_azul = randint(40,600)
y_azul = randint(50,430)
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo só que mais legal')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    tempo += 0.03
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
                if opcao == 1:
                    opcao = 0
                else:
                    opcao = 1


    if menu == 0:
        tela.fill((10,10,10))
        mensagem = 'Pygame - Testes'
        mensagem_2 = 'Jogar'
        mensagem_3 = 'Sair'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        tempo_formatado = fonte.render(mensagem_2, True, (opcao * 255,255,255))
        if opcao == 0:
            texto3_formatado = fonte.render(mensagem_3, True, (255,255,255))
        else:
            texto3_formatado = fonte.render(mensagem_3, True, (0,255,255))
        tela.blit(texto_formatado, (50, 0))
        tela.blit(tempo_formatado, (50, 70))
        tela.blit(texto3_formatado, (50, 120))
        if pygame.key.get_pressed()[K_SPACE]:
            tempo = 0
            if opcao == 1:
                menu = 1
            else:
                pygame.quit()
                exit()
            barulho_colisao.play()


    elif tempo <= 30 and tempo >= 0 and menu == 1:
        mensagem = f'Pontos: {pontos}'
        mensagem_2 = f'Tempo: {30-tempo:.1f}'
        texto_formatado = fonte.render(mensagem, True, (255,255,255))
        tempo_formatado = fonte.render(mensagem_2, True, (255,255,255))
        ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x, y, largura_obj, altura_obj))
        ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50))
        if pygame.key.get_pressed()[K_LEFT]:
            x -= 20
        if pygame.key.get_pressed()[K_RIGHT]:
            x += 20
        if pygame.key.get_pressed()[K_DOWN]:                        
            y += 20
        if pygame.key.get_pressed()[K_UP]:
            y -= 20
        if ret_vermelho.colliderect(ret_azul):
            x_azul = randint(40,600)
            y_azul = randint(50,430)
            pontos += 1
            barulho_colisao.play()

        tela.blit(texto_formatado, (450, 40))
        tela.blit(tempo_formatado, (450, 0))


    else:
        mensagem = f'Você fez {pontos} pontos!'
        mensagem_2 = f'O tempo acabou!'
        texto_formatado = fonte.render(mensagem, True, (0,0,255))
        tempo_formatado = fonte.render(mensagem_2, True, (255,0,0))
        tela.blit(tempo_formatado, (185, altura/2+a))
        tela.blit(texto_formatado, (180, altura/2+(altura+a)))
        if tempo >= 33 and tempo <= 34:
            a -= 15
        if tempo >= 35:
            menu = 1

    pygame.display.update()