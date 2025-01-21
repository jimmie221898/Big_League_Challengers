import pygame

pygame.init()

screen = pygame.display.set_mode((1800,900))

pygame.display.set_caption("Big League Challengers")
icon = pygame.image.load("Assets/Game_icon.png")
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()