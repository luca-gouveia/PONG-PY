import pygame
from pygame import *

class Object():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # ----BOLA_DIRECAO_VELOCIDADE--------
        self.speed_x = 7
        self.speed_y = 7

    def draw(self, screen, color):
        return pygame.draw.rect(screen, color, [self.x, self.y, self.width, self.height])

    def move_player(self, keys, player, height):
        if (player == 1):
            if (keys[pygame.K_w]):
                self.y -= 10
                if (self.y < 65):
                    self.y = 65
            if (keys[pygame.K_s]):
                self.y += 10
                if (self.y > height - (self.height + 35)):
                    self.y = height - (self.height + 35)  # Altura + altura da wall
        elif (player == 2):
            if (keys[pygame.K_UP]):
                self.y -= 10
                if (self.y < 65):
                    self.y = 65
            if (keys[pygame.K_DOWN]):
                self.y += 10
                if (self.y > height - (self.height + 35)):
                    self.y = height - (self.height + 35)

    def move_ball(self, height):
        self.x += self.speed_x
        self.y += self.speed_y

        if (self.y > height - 50):
            self.speed_y *= -1
        if (self.y < 70):
            self.speed_y *= -1

    def collide(self,player1_rect, player2_rect):
        if player1_rect.collidepoint(self.x, self.y):
            self.speed_x *= -1
            paddle_sound = pygame.mixer.Sound('sounds/pong_paddle.wav')
            paddle_sound.play()
        if player2_rect.collidepoint(self.x, self.y):
            self.speed_x *= -1
            paddle_sound = pygame.mixer.Sound('sounds/pong_paddle.wav')
            paddle_sound.play()

    #A FUNCAO ABAIXO FAZ A ANIMACAO DA BOLA NO MENU!        
    def move_ball_menu(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y

        if(self.x > width-self.width or self.x < 0):
            self.speed_x *= -1

        if(self.y > height-10 or self.y < 0):
            self.speed_y *= -1

        