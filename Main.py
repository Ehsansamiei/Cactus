# EHsan

# Libraries :
import pygame 

# Colors:
white = (255, 255, 255)
# Pygame setup :
pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
runnig = True
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
dt = 0
screen_width = screen.get_width()
screen_height = screen.get_height()
#################################################

cactus_frames = [
    # pygame.image.load('images/cactus1.png'),
    pygame.image.load('images/cactus-run1.png'),
    # pygame.image.load('images/cactus4.png'),
    pygame.image.load('images/cactus-run2.png'),
]
# change the size of frames
cactus_frames = [pygame.transform.scale(frame, (screen_width * 0.10, screen_height * 0.25)) for frame in cactus_frames]

cactus_frame_index = 0
cactus_animation_timer = 0
cactus_animation_speed = 0.2

cactus_y = screen_height * 0.93
cactus_velocity = 0
gravity = 2000
is_jumping = False
jump_force = -1000

#################################################
background = pygame.image.load('images/sky.png')
background_image = pygame.transform.scale(background,(screen_width, screen_height))
background_image_x = 0
#################################################
floor = pygame.image.load('images/floor2.png')
floor_image = pygame.transform.scale(floor,(screen_width, screen_height  / (100) * 8))
floor_image_x = 0
#################################################
quit_button = pygame.image.load('images/exit_btn.png')
quit_button_image = pygame.transform.scale(quit_button, (screen_width * (20) / 100, screen_height * (20) / 100))


#Button Class:
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        action = False 

        # get mouse position
        pos = pygame.mouse.get_pos()

        #check mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on the screen
        DISPLAYSURF.blit(self.image, (self.rect.x, self.rect.y))
        return action
    
# creat instance form button
exit_button = Button(screen_width * (1) / 100, screen_height * (2) / 100, quit_button_image, 0.35)


while runnig :
    for event in pygame.event.get():
        '''pygame.QUIT event means the user clicked X to close your window'''
        if event.type == pygame.QUIT:
            runnig = False

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and not is_jumping:
            cactus_velocity = jump_force
            is_jumping = True

    '''filll the screen with my background image'''
    screen.blit(background_image, (background_image_x, 0))
    screen.blit(background_image, (background_image_x + screen_width, 0))
    background_image_x -= 2
    if background_image_x <= -screen_width:
        background_image_x = 0

    screen.blit(floor_image, (floor_image_x, screen_height * (93) / 100))
    screen.blit(floor_image, (floor_image_x + screen_width, screen_height * (93) / 100))
    floor_image_x -= 5
    if floor_image_x <= -screen_width:
        floor_image_x = 0

    # update animation
    cactus_animation_timer += dt
    if cactus_animation_timer >= cactus_animation_speed:
        cactus_animation_timer = 0
        cactus_frame_index = (cactus_frame_index + 1) % len(cactus_frames)


    if exit_button.draw():
        # accident = True
        pygame.quit()
        quit()



    screen.blit(cactus_frames[cactus_frame_index], (0, cactus_y))
    # apply gravity
    cactus_velocity += gravity * dt
    cactus_y += cactus_velocity * dt

    # touch the floor
    
    ground_y = screen_height * 0.75
    if cactus_y >= ground_y:
        cactus_y = ground_y
        cactus_velocity = 0
        is_jumping = False

    # Render the game
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()