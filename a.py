import pygame, sys

pygame.init()

funZone = pygame.display.set_mode((400, 400))
posX = 200
posY = 200 

pygame.display.set_caption("Funzone :^)")
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

moveDown = False
moveUp = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moveUp = True
                moveDown = False
            if event.key == pygame.K_s:
                moveDown = True
                moveUp = False
    if moveUp and posY > 0:
        posY -= 5

    if moveDown and posY < 400-25:
        posY += 5
        


    funZone.fill(blue)
    pygame.draw.rect(funZone, red, (posX, posY, 25, 25), 0)
     
    pygame.display.update()
