import pygame
import time
import random
import menu

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sierpinski Triangle Fractal - Step by Step")

WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

count = 0

# Function to get a rainbow color based on depth
def get_color(depth):
    colors = [
        (255, 0, 0),   # Red
        (255, 165, 0), # Orange
        (255, 255, 0), # Yellow
        (0, 255, 0),   # Green
        (0, 0, 255),   # Blue
        (75, 0, 130),  # Indigo
        (238, 130, 238) # Violet
    ]
    return colors[depth % len(colors)]  # Cycle through rainbow colors

# Function to draw the Sierpinski Triangle step by step
def sierpinski(x, y, size, depth):
    if depth == 0:
        return
    else:
        # Get a color based on depth
        color = get_color(depth)

        # Draw the triangle with the color
        pygame.draw.polygon(screen, color, [(x, y),
                                            (x + size, y),
                                            (x + size / 2, y - size)], 1)
        pygame.display.update()  # Update after drawing the triangle
        time.sleep(0.05)  # Add a delay to make it visible step by step

        # Recursively draw 3 smaller triangles
        sierpinski(x, y, size / 2, depth - 1)
        sierpinski(x + size / 2, y, size / 2, depth - 1)
        sierpinski(x + size / 4, y - size / 2, size / 2, depth - 1)


# Function to run the fractal
def run_fractal():
    screen.fill(BACKGROUND_COLOR)  # Clear screen

    x = WIDTH // 4
    y = HEIGHT // 1.5
    size = WIDTH // 2
    depth = 6  # Set recursion depth (higher = more complex)

    # Draw the fractal step by step
    sierpinski(x, y, size, depth)

    pygame.display.update()  # Ensure the drawing appears

    # Wait for user to close after the fractal drawing
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_input = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting_for_input = False  # Exit after Enter key is pressed

    menu.show_continue_exit_screen()

# Run the fractal
if __name__ == "__main__":
    run_fractal()
