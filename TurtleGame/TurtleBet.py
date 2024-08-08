import pygame as pg, sys, random
pg.init()

class Turtle(pg.sprite.Sprite):

    def __init__(self,image,offset:tuple):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load(image)
        self.rect=self.image.get_rect()
        self.rect=self.rect.move(offset[0],offset[1])
        self.speed=3
        self.started=False
        self.finished=False
        self._counter=0

    def update(self):
        self._counter+=1
        if self._counter==60:
            r=random.randint(1,5)
            self.speed=r
            print(r)
            self._counter=0
        newpos=self.rect.move(self.speed,0)
        self.rect=newpos




SIZE=(1000,700)

screen=pg.display.set_mode(SIZE)
clock=pg.time.Clock()

wt=Turtle("TurtleGame/TurtWh.png",(0,500))

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
    wt.update()
    screen.fill((0,0,0))
    screen.blit(wt.image,wt.rect)
    pg.display.update()

    clock.tick(60)



