import pygame

# Button Constants
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
BUTTON_COLOR = (0, 0, 255)
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_TEXT = 'Show Velocity-Time Graph'

def create_button(window, width, height):
    button_position = ((width - BUTTON_WIDTH) / 2, height - BUTTON_HEIGHT - 20)
    button_rect = pygame.Rect(button_position[0], button_position[1], BUTTON_WIDTH, BUTTON_HEIGHT)
    return button_rect

def draw_button(window, button_rect):
    pygame.draw.rect(window, BUTTON_COLOR, button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render(BUTTON_TEXT, True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=button_rect.center)
    window.blit(text, text_rect)

def handle_button_event(event, button_rect):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):
            return True
    return False
