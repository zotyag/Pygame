import pygame, sys
pygame.init()

SIZE=(1000, 700)
screen=pygame.display.set_mode(SIZE)
clock=pygame.time.Clock()





while True:
    for keys in pygame.event.get():
        if keys.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K]









    pygame.display.update()
    clock.tick(60)






