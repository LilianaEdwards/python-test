import pygame as p
p.init()
scr = p.display.set_mode((600,500))
running = True
while running :
    for event in p.event.get() :
        if event.type == p.QUIT :
            running = False
    scr.fill((255,255,255))
    p.draw.circle(scr,(200,0,0),(250,250),80)
    p.display.flip()
p.quit()