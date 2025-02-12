import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fractals Menu")
depth = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VIBRANT_BLUE = (30, 144, 255)
DARK_BLUE = (0, 102, 204)
SKY_BLUE = (135, 206, 250)

# Fonts
title_font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 40)

# Button class
class Button:
    def __init__(self, x, y, width, height, text, text_color=WHITE, button_color=VIBRANT_BLUE, hover_color=DARK_BLUE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.button_color = button_color
        self.hover_color = hover_color
        self.is_hovered = False

    def draw(self, surface):
        current_color = self.hover_color if self.is_hovered else self.button_color
        pygame.draw.rect(surface, current_color, self.rect, border_radius=20)
        text_surface = button_font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos)

# Function to display fractals and transition to Continue/Exit screen
def fractal_display(fractal_function, *args):
    screen.fill(SKY_BLUE)  # Clear the screen before drawing
    pygame.display.flip()

    fractal_function(*args)  # Draw the fractal

    pygame.display.flip()  # Ensure the fractal is shown
    pygame.time.delay(2000)  # Delay to ensure the fractal appears completely

# Main menu function
def main_menu():
    button_width, button_height = 250, 75
    button_one = Button(275, 200, button_width, button_height, "Tree")
    button_two = Button(275, 300, button_width, button_height, "Snowflake")
    button_three = Button(275, 400, button_width, button_height, "Sierpinski")
    exit_button = Button(275, 500, button_width, button_height, "Exit")

    while True:
        screen.fill(SKY_BLUE)

        # Draw title
        title = title_font.render("Fractals", True, BLACK)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title, title_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if button_one.handle_event(event):
                import tree
                fractal_display(tree.draw_fractal_tree)
            elif button_two.handle_event(event):
                import snowflake  # Import only when Snowflake button is clicked
                fractal_display(snowflake.run_snowflake, depth)
            elif button_three.handle_event(event):
                import sierpinski  # Import only when Sierpinski button is clicked
                fractal_display(sierpinski.run_fractal)
            elif exit_button.handle_event(event):
                pygame.quit()
                sys.exit()

        button_one.draw(screen)
        button_two.draw(screen)
        button_three.draw(screen)
        exit_button.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
