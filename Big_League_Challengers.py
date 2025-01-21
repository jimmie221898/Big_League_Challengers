import pygame

pygame.init()

screen = pygame.display.set_mode((950,800))
pygame.display.set_caption("Big League Challengers")
icon = pygame.image.load("Assets/Game_icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
Game_Menu = pygame.image.load('Assets/Game_menu.png').convert()

running = True
while running:

    screen.blit(Game_Menu,(-60,-200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()