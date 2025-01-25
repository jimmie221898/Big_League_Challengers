import pygame
import button
import math

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


bullet_group = pygame.sprite.Group()
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        self.group = bullet_group
        pygame.sprite.Sprite.__init__(self, self.group)
        self.speed = 10 
        self.left_image = pygame.image.load("images/bullet_left.png").convert_alpha()
        self.right_image = pygame.image.load("images/bullet_right.png").convert_alpha()
        if direction == -1:
            self.image = self.left_image
        else:
            self.image = self.right_image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
        

    def update(self):
        #move bullet
        self.rect.x += (self.direction *self.speed)
        #check if bullet off screen
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

# =====CHARACTER CLASSES=====
class Character(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self. image_type = type
        self.idle_right = pygame.image.load(f"images/{self.image_type}_idle_right.png").convert_alpha()
        self.idle_left = pygame.image.load(f"images/{self.image_type}_idle_left.png").convert_alpha()
        self.jump_right = pygame.image.load(f"images/{self.image_type}_jump_right.png").convert_alpha()
        self.jump_left = pygame.image.load(f"images/{self.image_type}_jump_left.png").convert_alpha()
        self.run_right_0 = pygame.image.load(f"images/{self.image_type}_run_right_0.png").convert_alpha()
        self.run_right_1 = pygame.image.load(f"images/{self.image_type}_run_right_1.png").convert_alpha()
        self.run_right_2 = pygame.image.load(f"images/{self.image_type}_run_right_2.png").convert_alpha()
        self.run_left_0 = pygame.image.load(f"images/{self.image_type}_run_left_0.png").convert_alpha()
        self.run_left_1 = pygame.image.load(f"images/{self.image_type}_run_left_1.png").convert_alpha()
        self.run_left_2 = pygame.image.load(f"images/{self.image_type}_run_left_2.png").convert_alpha()
        self.glide_left = pygame.image.load(f"images/{self.image_type}_glide_left.png").convert_alpha()
        self.glide_right = pygame.image.load(f"images/{self.image_type}_glide_right.png").convert_alpha()
        self.run_right_images = [self.run_right_0, self.run_right_1, self.run_right_2, self.run_right_1]
        self.run_left_images = [ self.run_left_0,  self.run_left_1,  self.run_left_2,  self.run_left_1]
        self.frame_counter = 0
        self.frame_delay = 7
        self.width = self.idle_right.get_width()
        self.height = self.idle_right.get_height()
        self.surface = pygame.Surface((self.width,self.height))
        self.direction = "right"
        self.step_count = 0

    def shoot(self):
        if hero.direction == "right":
            bullet = Bullet(self.rect.centerx + 150, self.rect.centery + 125, 1)
        else:
            bullet = Bullet(self.rect.centerx - 50, self.rect.centery + 125, -1)  


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
        self.shoot_cooldown = 120

    def move(self, ground):
        keys = pygame.key.get_pressed()

        # Horizontal movement
        if keys[pygame.K_d]:
            self.direction = "right"
            self.x += self.x_speed
            if not self.jumping:
                screen.blit(self.run_right_images[self.frame_counter // self.frame_delay], (hero.x, hero.y)) 
                self.frame_counter = (self.frame_counter + 1) % (len(self.run_right_images) * self.frame_delay)  # Loop through frames
        elif keys[pygame.K_a]:
            self.direction = "left"
            self.x -= self.x_speed
            if not self.jumping:
                screen.blit(self.run_left_images[self.frame_counter // self.frame_delay], (hero.x, hero.y)) 
                self.frame_counter = (self.frame_counter + 1) % (len(self.run_left_images) * self.frame_delay)  # Loop through frames
        elif self.jumping == False:
            if self.direction == "right":
                screen.blit(self.idle_right, (hero.x, hero.y))  # Draw the hero at the new position
            else:
                screen.blit(self.idle_left, (hero.x, hero.y))  # Draw the hero at the new position
       
       
        # Start jumping
        if keys[pygame.K_SPACE] and self.on_ground:
            self.jumping = True
            self.on_ground = False
            self.y_jump_velocity = self.jump_height  # Reset jump velocity when starting a new jump

        # Handle jumping and gliding
        if self.jumping:
            if self.gliding:
                self.y -= self.y_jump_velocity
                self.y_jump_velocity -= self.glide_gravity
                # Display the gliding images
                if self.direction == "right":
                    screen.blit(self.glide_right, (hero.x, hero.y))
                else:
                    screen.blit(self.glide_left, (hero.x, hero.y))
                if not keys[pygame.K_SPACE]:
                    self.gliding = False
            else:
                self.y -= self.y_jump_velocity
                self.y_jump_velocity -= self.gravity
                # Display the jumping images
                if self.direction == "right":
                    screen.blit(self.jump_right, (hero.x, hero.y))
                else:
                    screen.blit(self.jump_left, (hero.x, hero.y))
                    
                if keys[pygame.K_SPACE] and self.y_jump_velocity < 0:
                    self.gliding = True

            # Ensure the character doesn't fall through the ground
            if self.rect.colliderect(ground) and self.y_jump_velocity < 0:
                self.jumping = False
                self.y_jump_velocity = self.jump_height
                self.velocity_y = 0
                self.y = ground.top  # Snap to the top of the ground

        else:  # Apply gravity and check for landing
            if not self.on_ground:
                self.velocity_y += self.gravity
                self.y += self.velocity_y

            # Check for collision with the ground
            if self.rect.colliderect(ground):
                self.on_ground = True
                self.jumping = False
                self.gliding = False
                self.y_jump_velocity = self.jump_height
                self.velocity_y = 0
                self.y = ground.top  # Keep the character on top of the ground
            else:
                self.on_ground = False

        # Prevent the character from ever going below the ground
        if self.y > ground.top:
            self.y = ground.top
            self.on_ground = True
            self.jumping = False
            self.velocity_y = 0
            self.gliding = False

        # Update rect for rendering
        self.rect.bottom = self.y
        self.rect.centerx = self.x
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:  # Left mouse button
            if self.shoot_cooldown == 0:
                hero.shoot()
                self.shoot_cooldown = 30
            print("Left mouse button is pressed")
        if mouse_buttons[1]:  # Middle mouse button
            print("Middle mouse button is pressed")
        if mouse_buttons[2]:  # Right mouse button
            print("Right mouse button is pressed")

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
            

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
        bullet_group.update()
        bullet_group.draw(screen)
        

    
        

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
            if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click
                if event.button == 1:  # Left mouse button
                    hero.shoot()
                    
    #endregion    


    pygame.display.flip()
    clock.tick(60)

pygame.quit()