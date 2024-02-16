import pygame as pg, sys, random
pg.init()

class Turtle(pg.sprite.Sprite):

    def __init__(self, image, offset: tuple):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(offset[0], offset[1])
        self.speed = 0
        self._new_speed = 2
        self.started = False
        self.finished = False
        self._counter = 0

    def update(self):
        self._counter += 1
        if self._counter == 60:
            r = random.randint(100, 400)
            self._new_speed = r / 100
            self._counter = 0
        if self.speed < self._new_speed:
            self.speed += 0.1
        elif self.speed > self._new_speed:
            self.speed -= 0.1
        newpos = self.rect.move(self.speed, 0)
        self.rect = newpos



class Finish(pg.sprite.Sprite):
    def __init__(self, pos: tuple,size:tuple,color:tuple):
        self.pos = pos
        self.surface=pg.surface.Surface((size))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.rect=self.rect.move(pos[0],pos[1])
        self.finished=False

    def crossed(self, *turtles):
        for turtle in turtles:
            if self.rect.colliderect(turtle.rect):
                print("True")
                self.finished=True






screen = pg.display.set_mode((1000, 700))
clock = pg.time.Clock()
finish=Finish((800, 170), (10, 480),(230,23,30))
finish_text_type=pg.font.Font(None,60)
finish_text=finish_text_type.render("FINISH",False,(230,23,30))
finish_text=pg.transform.rotate(finish_text,270)
finish.surface.blit(finish_text,finish_text.get_rect())

wt = Turtle("TurtWh.png", (0, 200))
bt = Turtle("TurtBl.png", (0, 300))
gt = Turtle("TurtGr.png", (0, 400))
rt = Turtle("TurtRe.png", (0, 500))
yt = Turtle("TurtYe.png", (0, 600))
turtles = pg.sprite.RenderPlain(wt, bt, gt, rt, yt)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE:
            pg.quit()
            sys.exit()


    if not finish.finished:
        turtles.update()
        screen.fill((0, 0, 0))
        screen.blit(wt.image, wt.rect)
        screen.blit(bt.image, bt.rect)
        screen.blit(gt.image, gt.rect)
        screen.blit(rt.image, rt.rect)
        screen.blit(yt.image, yt.rect)
        screen.blit(finish.surface,finish.rect)
        screen.blit(finish_text,finish.rect.move(10,-80).midright)
        finish.crossed(wt,bt,gt,rt,yt)


    pg.display.update()
    clock.tick(60)
    # print(clock.get_fps())
