import pygame


# Inicializando o pygame e criando a janela

pygame.init()

Tela = pygame.display.set_mode([1080, 720])
pygame.display.set_caption("PCA Game Sustentabilidade")

# carregando sprites

menu = pygame.image.load("Layout/Telas/fundo_tela_inicial.png")
ButtomStart = pygame.image.load("Layout/botoes/botão1.png")
ButtomExit = pygame.image.load("Layout/botoes/botão2.png")
ButtomCredits = pygame.image.load("Layout/botoes/botão3.png")
BG_game = pygame.image.load("Layout/Telas/FundoJogo.png")
lixeira_1 = pygame.image.load("Layout/lixeiras/lixeira_1.png")
lixeira_2 = pygame.image.load("Layout/lixeiras/lixeira_2.png")
lixeira_3 = pygame.image.load("Layout/lixeiras/lixeira_3.png")
lixeira_4 = pygame.image.load("Layout/lixeiras/lixeira_4.png")
lixeira_5 = pygame.image.load("Layout/lixeiras/lixeira_5.png")
lixeira_1g = pygame.image.load("Layout/lixeiras/lixeira_1g.png")
lixeira_2g = pygame.image.load("Layout/lixeiras/lixeira_2g.png")
lixeira_3g = pygame.image.load("Layout/lixeiras/lixeira_3g.png")
lixeira_4g = pygame.image.load("Layout/lixeiras/lixeira_4g.png")
lixeira_5g = pygame.image.load("Layout/lixeiras/lixeira_5g.png")
org_1 = pygame.image.load("Layout/lixo/banana.png")
org_1_pos = (795, 412)
org_2 = pygame.image.load("Layout/lixo/maca.png")
org_2_pos = (879, 419)
pla_1 = pygame.image.load("Layout/lixo/garrafadeplastico.png")
pla_1_pos = (1012, 493)
pla_2 = pygame.image.load("Layout/lixo/CDquebrado.png")
pla_2_pos = (860, 507)
pla_3 = pygame.image.load("Layout/lixo/pneufurado.png")
pla_3_pos = (707, 510)
vid_1 = pygame.image.load("Layout/lixo/garrafadevidro.png")
vid_1_pos = (400, 400)
vid_2 = pygame.image.load("Layout/lixo/oculosquebrado.png")
vid_2_pos = (500, 400)
pap_1 = pygame.image.load("Layout/lixo/caixadepapelao.png")
pap_1_pos = (594, 499)
pap_2 = pygame.image.load("Layout/lixo/caixaleite.png")
pap_2_pos = (448, 503)
pap_3 = pygame.image.load("Layout/lixo/caixinhadesuco.png")
pap_3_pos = (227, 505)
pap_4 = pygame.image.load("Layout/lixo/pacotedebiscoito.png")
pap_4_pos = (93, 406)
pap_5 = pygame.image.load("Layout/lixo/papeldebala.png")
pap_5_pos = (300, 400)
met_1 = pygame.image.load("Layout/lixo/latinha.png")
met_1_pos = (1020, 415)
met_2 = pygame.image.load("Layout/lixo/celularquebrado.png")
met_2_pos = (974, 423)

# desenhando sprites

Tela.blit(menu, (0, 0))
Tela.blit(ButtomStart, (520, 260))
Tela.blit(ButtomExit, (550, 420))
Tela.blit(ButtomCredits, (550, 550))


# colocando Musica

pygame.mixer.music.load("sons/music.wav")
pygame.mixer.music.play(-1)

# Funcionalidades do jogo

gameLoop = True
ingame = False

while gameLoop:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameLoop = False
# funcionalidade botões do menu

        if event.type == pygame.MOUSEBUTTONDOWN:
            MousePos = pygame.mouse.get_pos()
            print(pygame.mouse.get_pos())

            # ingame
            if 575 <= MousePos[0] <= 949 and 307 <= MousePos[1] <= 407 and not ingame:
                ingame = True
                print("Iniciando Game!")
                pygame.mixer.music.load("sons/happy.mp3")
                pygame.mixer.music.play(-1)

                # desenhando/organizando tela ingame
                print("Organizando Tela de jogo...")
                Tela.blit(BG_game, (0, 0))
                Tela.blit(lixeira_1, (60, 520))
                Tela.blit(lixeira_2, (260, 540))
                Tela.blit(lixeira_3, (460, 520))
                Tela.blit(lixeira_4, (660, 540))
                Tela.blit(lixeira_5, (860, 520))

                # colocando lixos no chão
                print("Jogando lixo no chão...")
                Tela.blit(org_1, org_1_pos)
                Tela.blit(org_2, org_2_pos)
                Tela.blit(met_1, met_1_pos)
                Tela.blit(met_2, met_2_pos)
                Tela.blit(pla_1, pla_1_pos)
                Tela.blit(pla_2, pla_2_pos)
                Tela.blit(pla_3, pla_3_pos)
                Tela.blit(pap_1, pap_1_pos)
                Tela.blit(pap_2, pap_2_pos)
                Tela.blit(pap_3, pap_3_pos)
                Tela.blit(pap_4, pap_4_pos)
                Tela.blit(pap_5, pap_5_pos)
                Tela.blit(vid_1, vid_1_pos)
                Tela.blit(vid_2, vid_2_pos)

            if 673 <= MousePos[0] <= 843 and 599 <= MousePos[1] <= 669 and not ingame:
                print("Créditos!")

            if 550 < MousePos[0] < (550 + 437) and 420 < MousePos[1] < (420 + 177) and not ingame:
                gameLoop = False

    pygame.display.update()
