import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lines")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up variables
lines = []
angle_range = (10, 80)
line_length = 50
line_speed = 2

# Define functions
def generate_line():
    # Generate a line at a random angle
    angle = random.uniform(*angle_range)
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = x1 + line_length * math.cos(math.radians(angle))
    y2 = y1 + line_length * math.sin(math.radians(angle))
    return ((x1, y1), (x2, y2))

def check_collision(line):
    # Check if a line collides with any existing lines
    for l in lines:
        if line != l and line_segment_intersection(line, l):
            return True
    return False

def line_segment_intersection(l1, l2):
    # Check if two line segments intersect
    x1, y1 = l1[0]
    x2, y2 = l1[1]
    x3, y3 = l2[0]
    x4, y4 = l2[1]
    den = (y4-y3)*(x2-x1)-(x4-x3)*(y2-y1)
    if den == 0:
        return False
    ua = ((x4-x3)*(y1-y3)-(y4-y3)*(x1-x3))/den
    ub = ((x2-x1)*(y1-y3)-(y2-y1)*(x1-x3))/den
    if ua >= 0 and ua <= 1 and ub >= 0 and ub <= 1:
        return True
    return False

# Start the game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Generate a new line
    line = generate_line()
    if not check_collision(line):
        lines.append(line)
    
    # Update lines
    for i in range(len(lines)):
        x1, y1 = lines[i][0]
        x2, y2 = lines[i][1]
        dx = line_speed * math.cos(math.atan2(y2-y1, x2-x1))
        dy = line_speed * math.sin(math.atan2(y2-y1, x2-x1))
        x1 += dx
        y1 += dy
        x2 += dx
        y2 += dy
        lines[i] = ((x1, y1), (x2, y2))
    
    # Draw lines
    screen.fill(white)
    for line in lines:
        pygame.draw.line(screen, black, line[0], line[1])
    pygame.display.flip()
    
    # Limit the fram rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
