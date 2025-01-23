import pygame
import button


pygame.init()

#VARIABLES
width = 950
height = 800
# Gravity and velocity
gravity = 1
velocity_y = 0
jump_height = 20
y_jump_velocity = jump_height
#define states
menu_state = "start"
previous_menu = "start"
game_paused = 1
running = True
jumping = False
#movement
character_move_amount = 4
x_change = 0
#character position
character_x = (width * 0.5)
character_y = (0)



#SETUP
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Big League Challengers")
icon = pygame.image.load("images/Game_icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
Game_Menu = pygame.image.load('images/Game_menu.png').convert()


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (211, 211, 211)
DARK_GRAY = (64, 64, 64)

RED = (255, 0, 0)
LIGHT_RED = (255, 102, 102)
DARK_RED = (139, 0, 0)

GREEN = (0, 255, 0)
LIGHT_GREEN = (144, 238, 144)
DARK_GREEN = (0, 100, 0)

BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 139)

YELLOW = (255, 255, 0)
LIGHT_YELLOW = (255, 255, 224)
DARK_YELLOW = (204, 204, 0)

ORANGE = (255, 165, 0)
LIGHT_ORANGE = (255, 200, 124)
DARK_ORANGE = (255, 140, 0)

PURPLE = (128, 0, 128)
LIGHT_PURPLE = (216, 191, 216)
DARK_PURPLE = (75, 0, 130)

PINK = (255, 192, 203)
HOT_PINK = (255, 105, 180)
LIGHT_PINK = (255, 182, 193)
DARK_PINK = (231, 84, 128)

BROWN = (139, 69, 19)
LIGHT_BROWN = (210, 180, 140)
DARK_BROWN = (101, 67, 33)

CYAN = (0, 255, 255)
LIGHT_CYAN = (224, 255, 255)
DARK_CYAN = (0, 139, 139)

MAGENTA = (255, 0, 255)
LIGHT_MAGENTA = (238, 130, 238)
DARK_MAGENTA = (139, 0, 139)

GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
BRONZE = (205, 127, 50)

#game scenes
Game_Menu = pygame.image.load('images/Game_menu.png').convert()

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

#character images
cat_image = pygame.image.load("images/cat_1.png").convert_alpha()
jump_cat_image_right = pygame.image.load("images/jump_cat.png").convert_alpha()
jump_cat_image_Left = pygame.image.load("images/jump_cat_left.png").convert_alpha()

#character sizes
character_width = cat_image.get_width()
character_height = cat_image.get_height()

def add_character_at_location(x,y,which_image):
    screen.blit(which_image,(x,y))



while running:

    screen.blit(Game_Menu,(-60,-200))

    #MENU STATE HANDLING
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

    if game_paused == False:
        character_rect = pygame.Rect(character_x, character_y, character_width, character_height)
        screen.fill(DARK_PINK)
        floor_rect = pygame.Rect(0, height - 100, width, 100)
        pygame.draw.rect(screen, LIGHT_GREEN, floor_rect)
        character_x += x_change
        
        keys = pygame.key.get_pressed()
        if game_paused == False:
            if keys[pygame.K_d]:  # Move right
                print("move right")
                x_change = +character_move_amount
            elif keys[pygame.K_a]:  # Move left
                print("move left")
                x_change = -character_move_amount
            else:  # If no movement key is pressed, stop movement
                x_change = 0
        

        #JUMPING
        if jumping:
            character_y -= y_jump_velocity
            y_jump_velocity -= gravity
            if y_jump_velocity < -jump_height:
                jumping = False
                y_jump_velocity = jump_height
            if keys[pygame.K_d]:  # Move right
                add_character_at_location(character_x,character_y,jump_cat_image_right)
            elif keys[pygame.K_a]:  # Move left
                add_character_at_location(character_x,character_y,jump_cat_image_Left)
            else:  # If no movement key is pressed, stop movement
                add_character_at_location(character_x,character_y,jump_cat_image_right)
            
        else:
            add_character_at_location(character_x,character_y,cat_image)
            if character_rect.colliderect(floor_rect):
                velocity_y = 0
            else:
                # Apply gravity
                velocity_y += gravity
                character_y += velocity_y

    #EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_paused == False:
            if event.type == pygame.KEYDOWN:
                print("key pressed")
                if event.key == pygame.K_ESCAPE:
                    menu_state = "pause"
                    game_paused = True
                    print("paused")
                if event.key == pygame.K_SPACE:
                    jumping = True
                


    pygame.display.flip()
    clock.tick(60)

pygame.quit()