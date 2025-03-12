import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Pool")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Font setup
font = pygame.font.Font(None, 36)  # Default font, size 36

# FPS control
clock = pygame.time.Clock()
FPS = 60  # Frames per second

# Game loop
running = True
preview = True


while running:






    screen.fill(WHITE)  # Clear screen
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit event
            running = False

        if event.type == pygame.KEYDOWN:  # Key press event
            if event.key == pygame.K_ESCAPE:  # Quit when pressing ESC
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse click event
            if preview:
                preview = False
            print(f"Mouse clicked at: {pygame.mouse.get_pos()}")  # Print mouse position

    
    
    ### Preview

    if preview:
        screen.fill((94, 204, 204))  # Clear screen
        p_img_x, p_img_y = 500, 500
        # Load image (make sure "image.png" is in the same folder or provide full path)
        image = pygame.image.load("PoolGame/images/pool_p.png")

        # Optional: Scale the image
        image = pygame.transform.scale(image, (p_img_x, p_img_y))  # Resize to 200x200 pixels

        # Draw the image at position (300, 200)
        screen.blit(image, (WIDTH/2 - (p_img_x/2), HEIGHT/2 - (p_img_y/2)))

        welcome_txt = font.render("Welcome to Pool!", True, BLACK)
        screen.blit(welcome_txt, (WIDTH/ 2 - welcome_txt.get_width()/2, 100))

        entry_txt = font.render("Click anywhere to begin!", True, BLACK)
        screen.blit(entry_txt, (WIDTH/ 2 - entry_txt.get_width()/2, HEIGHT-100))
    else:
        screen.fill((80, 255, 10))  # Clear screen
        


    
    # # Draw a rectangle
    # pygame.draw.rect(screen, RED, (WIDTH//2 - 50, HEIGHT//2 - 25, 100, 50))

    # # Display text
    # text_surface = font.render("Hello, Pygame!", True, BLACK)
    # screen.blit(text_surface, (WIDTH//2 - 80, HEIGHT//2 - 60))

    pygame.display.flip()  # Update display
    clock.tick(FPS)  # Limit frame rate

# Quit Pygame properly
pygame.quit()
