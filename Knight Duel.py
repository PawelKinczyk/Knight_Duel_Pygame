import random
import pygame
import math
from sys import exit
import os

# Thanks Kingsley from Stack for help

# Get the current working directory
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))


"""Class"""

class Knight(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direct):
        super().__init__()
        # Knight image depend of direction
        if direct == -1:
            self.image = pygame.image.load(
                r"C:\Users\pawel\Documents\GitHub\Geometry_War\Geometry_War\Geometry_War\Graphic\knight1.png").convert_alpha()
            self.rect = self.image.get_rect(midbottom=(pos_x, pos_y))
        else:
            self.image = pygame.image.load(
                r"C:\Users\pawel\Documents\GitHub\Geometry_War\Geometry_War\Geometry_War\Graphic\knight1.png").convert_alpha()
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect(midbottom=(pos_x, pos_y))

        # Old geometry
        # self.image= pygame.Surface([width, height])   # note: twice width to leave room for rotating spear
        # self.rect = self.image.get_rect()
        # self.rect.midbottom = ( pos_x, pos_y )
        # self.base_color  = color

        # Knight spear
        self.spear_color = (0, 0, 0)
        self.spear_length = 100  # pixels
        self.spear_angle = 180

        # Movement
        self.speed = 0
        self.direction = direct  # 1=right, -1=left

    def update(self):
        """ Move the horsey ... if we have any speed """
        self.rect.x += self.speed * self.direction

    def accelerate(self, amount=1):
        self.speed += amount + random.randint(0, 2)

    def decelerate(self, amount=1):
        self.speed -= amount + random.randint(0, 2)

    def setSpearPosition(self, angle):
        """ The user has adjusted the spear position, regenerate the Knight's image """

        self.spear_angle = angle


    def raiseSpear(self):
        self.setSpearPosition(self.spear_angle + 1 + random.randint(0, 2))

    def lowerSpear(self):
        self.setSpearPosition(self.spear_angle - 1 - random.randint(0, 2))


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            r"C:\Users\pawel\Documents\GitHub\Geometry_War\Geometry_War\Geometry_War\Graphic\ground.png").convert_alpha()
        # self.image = pygame.transform.scale(self.image, (800, 100))
        # self.image= pygame.Surface([800, 100])
        # self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [000, 344]


class Sky(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            r"C:\Users\pawel\Documents\GitHub\Geometry_War\Geometry_War\Geometry_War\Graphic\fortress1.png").convert()
        # self.image = pygame.transform.scale(self.image, (800, 100))
        # self.image= pygame.Surface([800, 100])
        # self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [0, 342]


# screen
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Knight Duel")
clock = pygame.time.Clock()
font = pygame.font.Font(r"C:\Users\pawel\Documents\GitHub\Geometry_War\Geometry_War\Geometry_War\Graphic\Pixeltype.ttf",50)
title_font = pygame.font.Font(r"C:\Users\pawel\Documents\GitHub\Geometry_War\Geometry_War\Geometry_War\Graphic\Pixeltype.ttf",100)

# start values
game_active = False
results = False
Knight1 = Knight(100, 341, 1)
Knight2 = Knight(700, 341, -1)
Knight1.spear_angle = 270
Knight2.spear_angle = 270
knight1_point=0
knight2_point=0
Knight1_score=0
Knight2_score=0
Ground = Ground()
Sky = Sky()

# Sprite group
background_group = pygame.sprite.Group()  # background group does not need to update
background_group.add(Sky, Ground)
knight_group = pygame.sprite.Group()
knight_group.add(Knight1, Knight2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # handle player input
        keys = pygame.key.get_pressed()
        # Moving knight
        if game_active:
            if event.type == pygame.KEYDOWN:
                #Moving knight

                if keys[pygame.K_d]:
                    Knight1.accelerate()
                if keys[pygame.K_a]:
                    Knight1.decelerate()

                if keys[pygame.K_LEFT]:
                    Knight2.accelerate()
                if keys[pygame.K_RIGHT]:
                    Knight2.decelerate()

                # Moving spear

                if keys[pygame.K_w]:
                    Knight1.raiseSpear()
                if keys[pygame.K_s]:
                    Knight1.lowerSpear()

                if keys[pygame.K_UP]:
                    Knight2.raiseSpear()
                if keys[pygame.K_DOWN]:
                    Knight2.lowerSpear()
                #Results for testing
                print("---RESULTS----")
                print("K1 " + str(Knight1.spear_angle) + "K2 " + str(Knight2.spear_angle))
                print("K1sp " + str(Knight1.spear_length) + "K2sp " + str(Knight2.spear_length))
                print("K1 xpocz " + str(Knight1.rect.x) + "K1 xkon " + str(K1_spear_point_x))
                print("K1 ypocz " + str(Knight1.rect.y) + "K1 ykon " + str(K1_spear_point_y))
                print(dist)
        else:
            if keys[pygame.K_SPACE]:
                game_active=True
    if game_active:
        """Get values at spear distance"""
        dist = pygame.math.Vector2(Knight1.rect.center).distance_to((Knight2.rect.center))
        if dist<20:
            if (Knight1.spear_angle >=346 and Knight1.spear_angle<=350) or (Knight1.spear_angle>= -14 and Knight1.spear_angle <=-9):
                knight1_point=1
            elif (Knight1.spear_angle >=351 and Knight1.spear_angle<=358) or (Knight1.spear_angle>= -8 and Knight1.spear_angle <=-5):
                knight1_point = 2
            elif (Knight1.spear_angle >=359 and Knight1.spear_angle<=360) or (Knight1.spear_angle>= -4 and Knight1.spear_angle <=-3) or(Knight1.spear_angle >=0 and Knight1.spear_angle<=4):
                knight1_point = 3
            elif (Knight1.spear_angle >= 5 and Knight1.spear_angle <= 19):
                knight1_point = 1
            elif (Knight2.spear_angle >=346 and Knight2.spear_angle<=350) or (Knight2.spear_angle>= -14 and Knight2.spear_angle <=-9):
                knight2_point=1
            elif (Knight2.spear_angle >=351 and Knight2.spear_angle<=358) or (Knight2.spear_angle>= -8 and Knight2.spear_angle <=-5):
                knight2_point = 2
            elif (Knight2.spear_angle >=359 and Knight2.spear_angle<=360) or (Knight2.spear_angle>= -4 and Knight2.spear_angle <=-3) or(Knight2.spear_angle >=0 and Knight2.spear_angle<=4):
                knight2_point = 3
            elif (Knight2.spear_angle >= 5 and Knight2.spear_angle <= 19):
                knight2_point = 1
            else:
                knight1_point = 0
                knight2_point = 0
            Knight1_score = Knight1.speed + knight1_point
            Knight2_score = Knight2.speed + knight2_point
            Knight1.rect.x=100
            Knight2.rect.x=700
            Knight1.speed=0
            Knight2.speed=0
            results=True
            game_active=False

        if Knight1.spear_angle>360:
            Knight1.spear_angle=0
        elif Knight2.spear_angle>360:
            Knight2.spear_angle=0
    # Draw the screen
        screen.fill(0)
        background_group.draw(screen)
        knight_group.update()
        knight_group.draw(screen)

        # Knight1 spear

        K1_spear_point_x = (Knight1.rect.x+Knight1.rect.width / 2) + (Knight1.spear_length * math.cos(math.radians(Knight1.spear_angle)))
        K1_spear_point_y = (Knight1.rect.y+ Knight1.rect.height / 2) + (Knight1.spear_length * math.sin(math.radians(Knight1.spear_angle)))
        pygame.draw.line(screen, Knight1.spear_color,
                         (Knight1.rect.x + Knight1.rect.width / 2, Knight1.rect.y + Knight1.rect.height / 2),
                         (K1_spear_point_x, K1_spear_point_y), 2)

        # Knight2 spear
        K2_spear_point_x = (Knight2.rect.x+Knight2.rect.width / 2) - (Knight2.spear_length * math.cos(math.radians(Knight2.spear_angle)))
        K2_spear_point_y = (Knight2.rect.y+ Knight2.rect.height / 2) + (Knight2.spear_length * math.sin(math.radians(Knight2.spear_angle)))
        pygame.draw.line(screen, Knight2.spear_color,
                         (Knight2.rect.x + Knight2.rect.width / 2, Knight2.rect.y + Knight2.rect.height / 2),
                         (K2_spear_point_x, K2_spear_point_y), 2)

    else:
        """Show menu"""
        screen.fill(0)
        background_group.draw(screen)

        #Text
        title = title_font.render("Knight Duel", False, 'Black')
        menu_mes = font.render("Press space to play", False, 'Black')
        ins1 = font.render("Knight1 move A / D Knight2 move Left / Right arrow", False, 'Black')
        ins2 = font.render("Knight1 spear W / S Knight2 spear Up / Down arrow", False, 'Black')

        title_rect = title.get_rect(center=(400, 100))
        ins1_rect = ins1.get_rect(center=(400, 190))
        ins2_rect = ins2.get_rect(center=(400, 240))
        menu_mes_rect = menu_mes.get_rect(center=(400, 300))

        if results==True:
            if Knight1_score>Knight2_score:
                score_mes = font.render("Knight1 won!", False, 'Black')
                score_mes_rect = score_mes.get_rect(center=(400, 200))
                screen.blit(score_mes, score_mes_rect)
                screen.blit(menu_mes, menu_mes_rect)
                screen.blit(title, title_rect)
            else:
                score_mes = font.render("Knight2 won!", False, 'Black')
                score_mes_rect = score_mes.get_rect(center=(400, 200))
                screen.blit(score_mes, score_mes_rect)
                screen.blit(menu_mes, menu_mes_rect)
                screen.blit(title, title_rect)
        else:
            screen.blit(ins1, ins1_rect)
            screen.blit(ins2, ins2_rect)
            screen.blit(menu_mes, menu_mes_rect)
            screen.blit(title, title_rect)


    pygame.display.update()
    clock.tick(60)
