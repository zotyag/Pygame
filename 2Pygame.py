import pygame, sys

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > 600:
            self.pos.left = 0

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()            #get a pygame clock object
player = pygame.image.load('intro_ball.gif').convert()
background = 0,0,0#pygame.image.load('background.bmp').convert()
screen.fill(background)
objects = []
for x in range(10):                    #create 10 objects</i>
    o = GameObject(player, x*40, x)
    objects.append(o)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for o in objects:
        screen.fill(background)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    clock.tick(60)
