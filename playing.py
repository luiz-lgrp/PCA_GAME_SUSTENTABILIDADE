from end_game import Game_Over
import pygame
from classes import Obj

Tela = pygame.display.set_mode([1080, 720])
def start_game():
    print("Iniciando Game!")
    acertos = 0
    erros = 0
    BG_game = Obj("Layout/Telas/FundoJogo.png", 0, 0)
    # Criando Lixeiras
    lixeira_1 = Obj("Layout/lixeiras/lixeira_1.png", 60, 520)
    lixeira_2 = Obj("Layout/lixeiras/lixeira_2.png", 260, 540)
    lixeira_3 = Obj("Layout/lixeiras/lixeira_3.png", 460, 520)
    lixeira_4 = Obj("Layout/lixeiras/lixeira_4.png", 660, 540)
    lixeira_5 = Obj("Layout/lixeiras/lixeira_5.png", 860, 520)

    # Criando lixos
    org_1 = Obj("Layout/lixo/banana.png", 795, 412)
    org_2 = Obj("Layout/lixo/maca.png", 879, 419)
    pla_1 = Obj("Layout/lixo/garrafadeplastico.png", 1012, 493)
    pla_2 = Obj("Layout/lixo/CDquebrado.png", 860, 507)
    pla_3 = Obj("Layout/lixo/pneufurado.png", 707, 510)
    vid_1 = Obj("Layout/lixo/garrafadevidro.png", 400, 400)
    vid_2 = Obj("Layout/lixo/oculosquebrado.png", 500, 400)
    pap_1 = Obj("Layout/lixo/caixadepapelao.png", 594, 499)
    pap_2 = Obj("Layout/lixo/caixaleite.png", 448, 503)
    pap_3 = Obj("Layout/lixo/caixinhadesuco.png", 227, 505)
    pap_4 = Obj("Layout/lixo/pacotedebiscoito.png", 93, 406)
    pap_5 = Obj("Layout/lixo/papeldebala.png", 300, 400)
    met_1 = Obj("Layout/lixo/latinha.png", 1020, 415)
    met_2 = Obj("Layout/lixo/celularquebrado.png", 974, 423)

    #Sons
    beepRight = pygame.mixer.Sound('sons/acertos.wav')
    beepRight.set_volume(0.4)
    beepWrong = pygame.mixer.Sound('sons/erros.wav')
    beepWrong.set_volume(2)
    pygame.mixer.music.load("sons/happy.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)


    # desenhando/organizando tela ingame
    print("Organizando Tela de jogo...")


    # colocando lixos no chão
    print("Jogando lixo no chão...")
    lixos = [org_1, org_2, met_1, met_2, pla_1, pla_2, pla_3, pap_1, pap_2, pap_3, pap_4, pap_5, vid_1, vid_2]

    id_lixo = 0

    plastico = [pla_1, pla_2, pla_3]
    organico = [org_1, org_2]
    metal = [met_1, met_2]
    papel = [pap_1, pap_2, pap_3, pap_4, pap_5]
    vidro = [vid_1, vid_2]

    loop = True
    drag = False

    while loop:
        BG_game.draw(Tela)
        lixeira_1.draw(Tela)
        lixeira_2.draw(Tela)
        lixeira_3.draw(Tela)
        lixeira_4.draw(Tela)
        lixeira_5.draw(Tela)

        for exist in lixos:
            exist.draw(Tela)

        for events in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if events.type == pygame.QUIT:
                return False
            if events.type == pygame.MOUSEBUTTONDOWN:
                print(f'Pegou no {pos}')
                for lixo in lixos:
                    if lixo.rect[0] <= pos[0] <= (lixo.rect[0] + lixo.rect[2]) and lixo.rect[1] <= pos[1] <= (lixo.rect[1] + lixo.rect[3]):
                        print(lixo.name)
                        id_lixo = lixos.index(lixo)
                        drag = True
            if events.type == pygame.MOUSEBUTTONUP:
                print(f'Largou no {pos}')
                drag = False
                if lixeira_1.rect[0] <= lixos[id_lixo].rect[0] <= (lixeira_1.rect[0] + lixeira_1.rect[2]) and lixeira_1.rect[1] <= lixos[id_lixo].rect[1] <= (lixeira_1.rect[1] + lixeira_1.rect[3]):
                    if lixos[id_lixo] in papel:
                        print('Acertou!!')
                        beepRight.play()
                        lixos[id_lixo].rect[0] = 2000
                        lixos[id_lixo].rect[1] = 2000
                        acertos += 1
                    else:
                        print('Errou!!')
                        beepWrong.play()
                        lixos[id_lixo].rect[0] = 700
                        lixos[id_lixo].rect[1] = 440
                        erros += 1
                if lixeira_2.rect[0] <= lixos[id_lixo].rect[0] <= (lixeira_2.rect[0] + lixeira_2.rect[2]) and lixeira_2.rect[1] <= lixos[id_lixo].rect[1] <= (lixeira_2.rect[1] + lixeira_2.rect[3]):
                    if lixos[id_lixo] in plastico:
                        print('Acertou!!')
                        beepRight.play()
                        lixos[id_lixo].rect[0] = 2000
                        lixos[id_lixo].rect[1] = 2000
                        acertos += 1
                    else:
                        print('Errou!!')
                        beepWrong.play()
                        lixos[id_lixo].rect[0] = 700
                        lixos[id_lixo].rect[1] = 440
                        erros += 1
                if lixeira_3.rect[0] <= lixos[id_lixo].rect[0] <= (lixeira_3.rect[0] + lixeira_3.rect[2]) and \
                        lixeira_3.rect[1] <= lixos[id_lixo].rect[1] <= (lixeira_3.rect[1] + lixeira_3.rect[3]):
                    if lixos[id_lixo] in metal:
                        print('Acertou!!')
                        beepRight.play()
                        lixos[id_lixo].rect[0] = 2000
                        lixos[id_lixo].rect[1] = 2000
                        acertos += 1
                    else:
                        print('Errou!!')
                        beepWrong.play()
                        lixos[id_lixo].rect[0] = 700
                        lixos[id_lixo].rect[1] = 440
                        erros += 1
                if lixeira_4.rect[0] <= lixos[id_lixo].rect[0] <= (lixeira_4.rect[0] + lixeira_4.rect[2]) and \
                        lixeira_4.rect[1] <= lixos[id_lixo].rect[1] <= (lixeira_4.rect[1] + lixeira_4.rect[3]):
                    if lixos[id_lixo] in vidro:
                        print('Acertou!!')
                        beepRight.play()
                        lixos[id_lixo].rect[0] = 2000
                        lixos[id_lixo].rect[1] = 2000
                        acertos += 1
                    else:
                        print('Errou!!')
                        beepWrong.play()
                        lixos[id_lixo].rect[0] = 700
                        lixos[id_lixo].rect[1] = 440
                        erros += 1
                if lixeira_5.rect[0] <= lixos[id_lixo].rect[0] <= (lixeira_5.rect[0] + lixeira_5.rect[2]) and \
                        lixeira_5.rect[1] <= lixos[id_lixo].rect[1] <= (lixeira_5.rect[1] + lixeira_5.rect[3]):
                    if lixos[id_lixo] in organico:
                        print('Acertou!!')
                        beepRight.play()
                        lixos[id_lixo].rect[0] = 2000
                        lixos[id_lixo].rect[1] = 2000
                        acertos += 1
                    else:
                        print('Errou!!')
                        beepWrong.play()
                        lixos[id_lixo].rect[0] = 700
                        lixos[id_lixo].rect[1] = 440
                        erros += 1
            if events.type == pygame.MOUSEMOTION:
                if drag:
                    lixos[id_lixo].move_obj(events)
        if acertos == len(lixos):
            Game_Over(erros, Tela)
            return False
        lixos[id_lixo].draw(Tela)
        pygame.display.update()
