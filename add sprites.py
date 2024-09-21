import pygame


pygame.init()


WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Movement Game")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  
RED = (255, 0, 0)   


sprite_size = 50
movable_sprite_pos = [100, 100]  
static_sprite_pos = [400, 200]   

running = True
while running:
    
    screen.fill(WHITE)

    
    pygame.draw.rect(screen, RED, (static_sprite_pos[0], static_sprite_pos[1], sprite_size, sprite_size))

    
    pygame.draw.rect(screen, BLUE, (movable_sprite_pos[0], movable_sprite_pos[1], sprite_size, sprite_size))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        movable_sprite_pos[0] -= 5  
    if keys[pygame.K_RIGHT]:
        movable_sprite_pos[0] += 5  
    if keys[pygame.K_UP]:
        movable_sprite_pos[1] -= 5  
    if keys[pygame.K_DOWN]:
        movable_sprite_pos[1] += 5  

    
    movable_sprite_pos[0] = max(0, min(movable_sprite_pos[0], WIDTH - sprite_size))
    movable_sprite_pos[1] = max(0, min(movable_sprite_pos[1], HEIGHT - sprite_size))

    
    pygame.display.flip()


pygame.quit()
