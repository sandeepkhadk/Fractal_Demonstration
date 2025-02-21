import pygame
import math
import sys
import random
import menu

WIDTH, HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Fractal Tre")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)

# Coordinate Transformation
def to_screen(pos):
    """Convert tree coordinates to Pygame screen coordinates."""
    x, y = pos
    screen_x = WIDTH // 2 + x
    screen_y = HEIGHT // 2 - y
    return (int(screen_x), int(screen_y))

# Recursive Tree Drawing
def tree_commands(length, pos, angle, branch_color):
    """Generates commands to draw a fractal tree using recursion."""
    if length < 10:
        return
    rad = math.radians(angle)
    new_x = pos[0] + length * math.cos(rad)
    new_y = pos[1] + length * math.sin(rad)
    new_pos = (new_x, new_y)

    yield ("line", pos, new_pos, branch_color, 2)
    yield ("circle", new_pos, 2, ORANGE) # Small leaf-like dot

    new_length = length * 0.75
    yield from tree_commands(new_length, new_pos, angle + 30, BROWN)
    yield from tree_commands(new_length, new_pos, angle - 30, BROWN)

# Function to Draw the Fractal Tree
def draw_fractal_tree():
    start_pos = (0, -100)
    start_angle = 90
    branch_length = 100
    cmd_gen = tree_commands(branch_length, start_pos, start_angle, GREEN)
    commands = []

    running = True
    # Drawing the fractal tree
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()  # Quit immediately if escape or window close
                return

        try:
            for _ in range(3):  # Process 3 recursive steps per frame
                cmd = next(cmd_gen)
                commands.append(cmd)
        except StopIteration:
            break  # Break when the fractal tree is fully drawn

        screen.fill(BLACK)

        # Draw the fractal tree based on commands
        for cmd in commands:
            if cmd[0] == "line":
                _, start, end, color, width = cmd
                pygame.draw.line(screen, color, to_screen(start), to_screen(end), width)
            elif cmd[0] == "circle":
                _, center, radius, color = cmd
                pygame.draw.circle(screen, color, to_screen(center), radius)

        pygame.display.flip()

    # Wait for user to press Enter to exit after the fractal is drawn
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_input = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting_for_input = False  # Exit after Enter key is pressed

    menu.show_continue_exit_screen()
# Ensure the script runs only when executed directly
if __name__ == "__main__":
    draw_fractal_tree()
