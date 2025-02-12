import pygame
import math
import conti
# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Koch Snowflake Fractal ❄️")

WHITE = (255, 255, 255)
BLUE = (100, 150, 255)
BLACK = (0, 0, 0)

# Function to draw Koch snowflake recursively
def koch_snowflake(order, p1, p2):
    if order == 0:
        pygame.draw.line(screen, BLUE, p1, p2, 2)
    else:
        x1, y1 = p1
        x2, y2 = p2

        dx, dy = (x2 - x1) / 3, (y2 - y1) / 3
        pA = (x1 + dx, y1 + dy)
        pB = (x1 + 2 * dx, y1 + 2 * dy)

        # Calculate peak of the triangle
        angle = math.radians(60)
        px = pA[0] + (dx * math.cos(angle)) - (dy * math.sin(angle))
        py = pA[1] + (dx * math.sin(angle)) + (dy * math.cos(angle))
        pC = (px, py)

        # Recursively draw smaller snowflake segments
        koch_snowflake(order - 1, p1, pA)
        koch_snowflake(order - 1, pA, pC)
        koch_snowflake(order - 1, pC, pB)
        koch_snowflake(order - 1, pB, p2)

# Function to draw the full Koch snowflake
def draw_snowflake(order):
    screen.fill(BLACK)

    # Define the main triangle vertices
    size = 300
    center_x, center_y = WIDTH // 2, HEIGHT // 2 + 50
    p1 = (center_x - size // 2, center_y + size // 3)
    p2 = (center_x + size // 2, center_y + size // 3)
    p3 = (center_x, center_y - 2 * size // 3)

    # Draw 3 sides of the snowflake
    koch_snowflake(order, p1, p2)
    koch_snowflake(order, p2, p3)
    koch_snowflake(order, p3, p1)

    pygame.display.flip()  # Use flip() for better rendering

# Function to run the snowflake simulation
def run_snowflake(depth):
    running = True
    current_depth = 0  # Start from depth 0

    while running and current_depth <= depth:
        pygame.time.delay(1000)  # Adjust speed of recursion increase

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit loop when user wants to close window

        draw_snowflake(current_depth)
        current_depth += 1  # Gradually increase depth over time

    # Wait for Enter key to quit after fractal drawing is complete
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_input = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting_for_input = False  # Exit after Enter key is pressed

    conti.show_continue_exit_screen()

# Run with a fixed depth (Change to desired depth)
run_snowflake(depth=5)
