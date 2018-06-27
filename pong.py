import sys, pygame
from pygame import *
from random import *
from objects import Object

pygame.init()
pygame.font.init()

def main_song():
    file = "sounds/main_song.wav"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    return(pygame.mixer.music.play())

def main_song_stop():
	return (pygame.mixer.music.stop())

main_song()

#---------CORES---------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (102, 102, 255)
YELLOW = (255, 255, 102)
color = WHITE

#TELA
width = 700
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)              # DEFININDO O TAMANHO DE TELA
pygame.display.set_caption("PONG-PY")

clock = pygame.time.Clock()                         # TAXA DE ATUALIZACAO

#PARTE_ESCRITA
pp1 = 0 #PONTOS DO PLAYER 1
pp2 = 0 #PONTOS DO PLAYER 2
win = 0

myfont = pygame.font.SysFont(None, 50)
myfont2 = pygame.font.SysFont(None, 30)
myfont_main = pygame.font.SysFont(None,80)

#CRIACAO DOS OBJETOS
player1 = Object(0, 210, 20, 100)
player2 = Object(width-20, 210, 20, 100)

ball = Object(width/2, 90, 10, 10)
ball2 = Object(width/2, 90, 10, 10)

wall_top = Object(0, 65, width, 10)
wall_bottom = Object(0, height-35, width, 10)

vertical_line = Object(width/2, 65, 3, height-90)

black_rec = Object(width/2 - 170, height/2-8,350,65)

main_screen = Object(0, 0, width,height)

start = 'MENU'

#LOOP DO JOGO
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # ---------------------MAIN SCREEN --------------------------------------------------

    if(start == 'MENU'): #ESTADO DE MENU    	
        main_screen.draw(screen, BLACK)

        PONG = myfont_main.render('PONG-PY', True, WHITE)
        START_m = myfont2.render('APERTE \'E\' PARA INICIAR', True, WHITE)
        START_mp = myfont2.render('APERTE \'P\' PARA PAUSAR', True, WHITE)

        screen.blit(PONG, (width / 2 - 120, height / 2 - 120))
        screen.blit(START_mp, (width / 2 - 120, height / 2 - 30))
        screen.blit(START_m, (width / 2 - 120, height / 2 - 52))
        ball2.draw(screen, color)
        ball2.move_ball_menu(width,height)

    if(start == 'PAUSE'):
        pause1 = myfont.render('PAUSADO', True, WHITE)
        pause2 = myfont2.render('APERTE \'E\' PARA RETOMAR', True, WHITE)
        black_rec.draw(screen, BLACK)
        screen.blit(pause1, (width / 2-80, height/ 2))
        screen.blit(pause2, (width / 2 - 130, height/2 + 35))
        main_song_stop()

    if (keys[pygame.K_e]): #SE TECLAR 'E' O JOGO INICIA(OU RETOMA)
        start = 'GAME'

    if(start == 'GAME'):
        screen.fill(BLACK)

        title = myfont.render("PONG-PY", True, WHITE)
        p1_points = myfont.render(str(pp1), True, YELLOW)
        p2_points = myfont.render(str(pp2), True, BLUE)

        screen.blit(title, ((width / 2) - 72, 10))
        screen.blit(p1_points, (80, 10))
        screen.blit(p2_points, (width - 80, 10))
        main_song_stop()

        #PAUSA 
        if(keys[pygame.K_p]):
            start = 'PAUSE'

        #---------------- DESENHANDO OS OBJETOS E MOVIMENTANDO-OS ------------------

        player1_rect = player1.draw(screen, WHITE)
        player2_rect = player2.draw(screen, WHITE)
        player1.move_player(keys, 1, height)
        player2.move_player(keys, 2, height)

        ball.draw(screen, color)
        ball.move_ball(height)

        wall_top.draw(screen,WHITE)
        wall_bottom.draw(screen,WHITE)

        vertical_line.draw(screen,WHITE)

        #------------------ COLISOES ------------------------------------------------

        ball.collide(player1_rect,player2_rect)

        #----------------- GERAR BOLA(QUANDO FAZ PONTO OU INICIA O JOGO) ------------

        if(win == 0):
            if (ball.x > width):
                ball.x = width / 2 + (randint(20, 50))
                ball.y = randint(90, 100)
                ball.speed_x *= -1
                point_sound = pygame.mixer.Sound('sounds/pong_point.wav')
                point_sound.play()
                pp1 += 1

            elif (ball.x < 0):
                ball.x = width / 2
                ball.y = randint(90, 100)
                ball.speed_x *= -1
                point = pygame.mixer.Sound('sounds/pong_point.wav')
                point.play()
                pp2 += 1

        # ----------------- FINAL/PONTOS/GANHADOR --------------------------------------

        end1 = myfont.render('PLAYER 1 GANHOU!!!', True, YELLOW)
        res = myfont2.render('APERTE \'SPACE\' PARA RECOMEÇAR', True, WHITE)

        end2 = myfont.render('PLAYER 2 GANHOU!!!', True, BLUE)
        res = myfont2.render('APERTE \'SPACE\' PARA RECOMEÇAR', True, WHITE)


        if(pp1 == 5):
            black_rec.draw(screen, BLACK)
            screen.blit(end1, (width/2 - 170, height/2))
            screen.blit(res, (width / 2 - 170, height / 2 + 35))
            win = 1
            color = BLACK
            if (keys[pygame.K_SPACE]):
                player1.x = 0
                player1.y = 210
                player2.x = width-20
                player2.y = 210
        
        if (pp2 == 5):
            black_rec.draw(screen, BLACK)
            screen.blit(end2, (width / 2 - 170, height / 2))
            screen.blit(res, (width / 2 - 170, height / 2 + 35))
            win = 1
            color = BLACK
            if (keys[pygame.K_SPACE]):
                player1.x = 0
                player1.y = 210
                player2.x = width-20
                player2.y = 210

        #-------------------- RESTART --------------------------------------------------

        if(keys[pygame.K_SPACE]):
            pp1 = 0
            pp2 = 0
            win = 0
            color = WHITE #COR DA BOLA

    #ATUALIZACAO
    pygame.display.flip()                           
    clock.tick(60)

