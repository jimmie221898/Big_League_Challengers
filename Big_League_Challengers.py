import pygame
import button

pygame.init()

screen = pygame.display.set_mode((950,800))
pygame.display.set_caption("Big League Challengers")
icon = pygame.image.load("images/Game_icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
Game_Menu = pygame.image.load('images/Game_menu.png').convert()

#define states
menu_state = "start"
previous_menu = "start"
game_paused = 1
running = True

#define fonts
font = pygame.font.SysFont("arialblack",40)

#load button images
resume_image = pygame.image.load("images/button_resume.png").convert_alpha()
options_image = pygame.image.load("images/button_options.png").convert_alpha()
quit_image = pygame.image.load("images/button_quit.png").convert_alpha()
video_image = pygame.image.load('images/button_video.png').convert_alpha()
audio_image = pygame.image.load('images/button_audio.png').convert_alpha()
keys_image = pygame.image.load('images/button_keys.png').convert_alpha()
back_image = pygame.image.load('images/button_back.png').convert_alpha()
start_image = pygame.image.load('images/button_start.png').convert_alpha()

#button instances
resume_button = button.Button(304,125,resume_image,1)
options_button = button.Button(297,250,options_image,1)
quit_button = button.Button(336,375,quit_image,1)
video_button = button.Button(226, 75, video_image, 1)
audio_button = button.Button(225, 200, audio_image, 1)
keys_button = button.Button(246, 325, keys_image, 1)
back_button = button.Button(332, 450, back_image, 1)
start_button = button.Button(304, 125, start_image, 1)


while running:

    screen.blit(Game_Menu,(-60,-200))

    if game_paused == True:
        #check menu state for main
        if menu_state == "start":
            if start_button.draw(screen):
                pygame.time.wait(100)
                game_paused = False
            if options_button.draw(screen):
                previous_menu = "start"
                menu_state = "options"
                pygame.time.wait(100)
            if quit_button.draw(screen):
                running = False
        #check menu state for options
        if menu_state == "options":
            if video_button.draw(screen):
                print("Video Settings")
            if audio_button.draw(screen):
                print("Audio Settings")
            if keys_button.draw(screen):
                print("Change Key Bindings")
            if back_button.draw(screen):
                if previous_menu == "start":
                    menu_state = "start"
                if previous_menu == "pause":
                    menu_state = "pause"
                previous_menu = "options"
                pygame.time.wait(100)
        #check menu state for pause
        if menu_state == "pause":
            if resume_button.draw(screen):
                game_paused = False
            if options_button.draw(screen):
                previous_menu = "pause"
                menu_state = "options"
                pygame.time.wait(100)
            if quit_button.draw(screen):
                running = False

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_paused == False:
            if event.key == pygame.K_ESCAPE:
                menu_state = "pause"
                game_paused = True


    pygame.display.flip()

pygame.quit()