import pygame
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
#Button class
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

# Function to clear the screen before showing the continue/exit menu
def clear_screen():
    screen.fill(SKY_BLUE)
    pygame.display.flip()

# Function to show Continue and Exit buttons after fractal is drawn
def show_continue_exit_screen():
    continue_button = Button(275, 250, 250, 75, "Continue")
    exit_button = Button(275, 350, 250, 75, "Exit")

    while True:
        screen.fill(SKY_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle button events
            if continue_button.handle_event(event):
                return  # Go back to the menu
            if exit_button.handle_event(event):
                pygame.quit()
                sys.exit()

            # Check for Enter key press to simulate clicking Continue
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return  # Go back to the menu

        continue_button.draw(screen)
        exit_button.draw(screen)
        pygame.display.flip()
