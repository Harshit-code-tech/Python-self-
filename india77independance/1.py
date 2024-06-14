import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Independence Day Celebration")

# Colors
saffron = (255, 153, 51)
white = (255, 255, 255)
green = (19, 136, 8)

# Clear the screen
screen.fill(white)

# Load Ashoka Chakra image
chakra_image = pygame.image.load("python\india77independance\chakra.png")
chakra_rect = chakra_image.get_rect(center=(screen_width // 2, screen_height // 2))

# Flag parameters
stripe_height = screen_height // 3
flag_frames = 30  # Number of frames in the waving animation

# Main loop
running = True
frame_count = 0  # Counter for the waving animation
rotation_angle = 0  # Angle for Ashoka Chakra rotation

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Draw the waving flag
    for i in range(3):
        color = saffron if i == 0 else white if i == 1 else green
        pygame.draw.rect(screen, color, (0, i * stripe_height + frame_count, screen_width, stripe_height))

    # Rotate the Ashoka Chakra
    rotated_chakra = pygame.transform.rotate(chakra_image, rotation_angle)
    rotated_rect = rotated_chakra.get_rect(center=chakra_rect.center)

    # Display the rotated Chakra
    screen.blit(rotated_chakra, rotated_rect)

    # Update display
    pygame.display.flip()

    # Update animation and rotation values
    frame_count = (frame_count + 1) % flag_frames
    rotation_angle = (rotation_angle + 1) % 360

# Clean up
pygame.quit()
sys.exit()
