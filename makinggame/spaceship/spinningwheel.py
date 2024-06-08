import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

# Load the background image
background_image = pygame.image.load("/Users/noahjaceortikov/Desktop/preply/makinggame/yesno.png")  # Replace "background.jpg" with the actual path to your background image

# Load the arrow image
arrow_image = pygame.image.load("/Users/noahjaceortikov/Desktop/preply/makinggame/rocket1.png")  # Replace "arrow.png" with the actual path to your arrow image

# Clock for controlling frame rate
clock = pygame.time.Clock()

def draw_rotated_arrow(angle, center):
    """Draws the arrow image rotated at the center position."""
    rotated_arrow = pygame.transform.rotate(arrow_image, angle)
    rect = rotated_arrow.get_rect(center=center)
    screen.blit(rotated_arrow, rect)

def main():
    running = True
    spinning = False
    angle = 0
    spin_speed = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not spinning:
                    spinning = True
                    spin_speed = random.randint(20, 40)  # Initial random speed

        # Draw the background
        screen.blit(background_image, (0, 0))

        if spinning:
            angle += spin_speed
            spin_speed *= 0.97  # Gradual slowdown of the spin
            if spin_speed < 0.5:
                spinning = False

        # Draw the rotated arrow
        draw_rotated_arrow(angle, (width // 2, height // 2))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
