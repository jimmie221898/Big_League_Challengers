import pygame
import button


pygame.init()

BASE_SPEED = 4
BASE_HEALTH = 150
WIDTH = 950
HEIGHT = 800
#define states
menu_state = "start"
previous_menu = "start"
game_paused = 1
running = True



#SETUP
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Big League Challengers")
icon = pygame.image.load("images/Game_icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
Game_Menu = pygame.image.load('images/Game_menu.png').convert()


#region Define colors
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
#endregion

#region game defines
#game scenes
Game_Menu = pygame.image.load('images/Game_menu.png').convert()

#define fonts
font = pygame.font.SysFont("arialblack",40)

#load buttons
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
#endregion

# =====CHARACTER CLASSES=====
class Character(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.idle_right = pygame.image.load("images/cat_idle_right.png").convert_alpha()
        # self.idle_left = pygame.image.load("images/{type}_idle_left.png").convert_alpha()
        # self.jump_right = pygame.image.load("images/{type}_jump_right.png").convert_alpha()
        # self.jump_left = pygame.image.load("images/{type}_jump_left.png").convert_alpha()
        # self.run_right_0 = pygame.image.load("images/{type}_run_right_0.png").convert_alpha()
        # self.run_right_1 = pygame.image.load("images/{type}_run_right_1.png").convert_alpha()
        # self.run_right_2 = pygame.image.load("images/{type}_run_right_2.png").convert_alpha()
        # self.run_left_0 = pygame.image.load("images/{type}_run_left_0.png").convert_alpha()
        # self.run_left_1 = pygame.image.load("images/{type}_run_left_1.png").convert_alpha()
        # self.run_left_2 = pygame.image.load("images/{type}_run_left_2.png").convert_alpha()
        self.width = self.idle_right.get_width()
        self.height = self.idle_right.get_height()
        self.surface = pygame.Surface((self.width,self.height))
        self.direction = "right"
        self.step_count = 0


class Hero(Character):
    def __init__(self):
        super().__init__("cat")
        self.rect = self.surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.x_speed = BASE_SPEED
        self.health = BASE_HEALTH
        self.gravity = 1
        self.velocity_y = 0
        self.jump_height = 25
        self.y_jump_velocity = self.jump_height
        self.jumping = False
        self.gliding = False
        self.on_ground = False
        self.glide_gravity = 0.01
        self.x = WIDTH / 2
        self.y = HEIGHT / 2

    def move(self, ground):
        keys = pygame.key.get_pressed()
        #print(self.y_jump_velocity)
        if keys[pygame.K_d]:
            self.direction = "right"
            self.x += self.x_speed
            self.rect = self.surface.get_rect(center=(self.x, self.y))
            screen.blit(self.idle_right, (self.x, self.y))
        elif keys[pygame.K_a]:
            self.direction = "left"
            self.x -= self.x_speed
            self.rect = self.surface.get_rect(center=(self.x, self.y))
            screen.blit(self.idle_right, (self.x, self.y))
        if keys[pygame.K_SPACE]:
            self.jumping = True

        if self.jumping:
            self.on_ground = False
            if self.gliding:
                self.y -= self.y_jump_velocity
                self.y_jump_velocity -= self.glide_gravity
                if not keys[pygame.K_SPACE]:
                    self.gliding = False
                 
            else:
                self.y -= self.y_jump_velocity
                self.y_jump_velocity -= self.gravity
                if keys[pygame.K_SPACE] and self.y_jump_velocity < 0:
                    self.gliding = True

            if ground.top - self.rect.bottom < 10 and self.y_jump_velocity < 0:
                self.gliding = False

            # Ground collision detection
            if self.rect.colliderect(ground) and self.y_jump_velocity < 14:
                self.jumping = False
                self.y_jump_velocity = self.jump_height
                self.velocity_y = 0
            
        else:
            # Check for collision with the ground
            if self.rect.colliderect(ground) and not self.on_ground:
                self.on_ground = True
                self.velocity_y = 0
                self.gliding = False  # Reset gliding when on the ground
            elif not self.on_ground:
                # Apply gravity or reduced gravity
                self.velocity_y += self.gravity
                self.y += self.velocity_y

        # Update rect for rendering
        self.rect.center = (self.x, self.y)
     
# class Zombie(Character):
#     def __init__(self):
#         Character.__init__(self, "Zombie")        
#         self.rect = self.surface.get_rect(center = (random.randint(50, WIDTH-50), random.randint(75,HEIGHT-75)))
#         self.x_speed = random.randint(1,5)
#         self.y_speed = random.randint(1,5)
    
    
#     def move(self):
#         if self.step_count >= 59:
#             self.step_count = 0

#         self.rect.move_ip(self.x_speed, self.y_speed)

#         if (self.rect.right > WIDTH) or (self.rect.left < 0):
#             self.x_speed *= -1
#             self.direction *= -1

#         if (self.rect.bottom > HEIGHT) or (self.rect.top < 0):
#             self.y_speed *= -1

#         self.step_count += 1


hero = Hero() 

while running:

    screen.blit(Game_Menu,(-60,-200))

    #region MENU STATE HANDLING
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
    #endregion
    if game_paused == False:
        screen.fill(DARK_PINK)
        floor_rect = pygame.Rect(0, HEIGHT - 100, WIDTH, 100)
        pygame.draw.rect(screen, LIGHT_GREEN, floor_rect)
    
        hero.move(floor_rect)  # Update the hero's position
        screen.blit(hero.surface, (hero.x, hero.y))  # Draw the hero at the new position

        

    # region EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_paused == False:
            if event.type == pygame.KEYDOWN:
                #print("key pressed")
                if event.key == pygame.K_ESCAPE:
                    menu_state = "pause"
                    game_paused = True
                    #print("paused")
    #endregion    


    pygame.display.flip()
    clock.tick(60)

pygame.quit()