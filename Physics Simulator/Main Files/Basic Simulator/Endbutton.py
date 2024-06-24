import pygame

# Button Constants
BUTTON_WIDTH, BUTTON_HEIGHT = 50, 50
BUTTON_COLOR = (255, 50, 50)
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_TEXT = 'End'

def create_Endbutton(window,width,height):
    button_position = (800,0)
    button_rect = pygame.Rect(button_position[0], button_position[1], BUTTON_WIDTH, BUTTON_HEIGHT)
    return button_rect

def draw_Endbutton(window,button_rect):
    pygame.draw.rect(window, BUTTON_COLOR, button_rect)
    font = pygame.font.Font(None, 20)
    text = font.render(BUTTON_TEXT, True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=button_rect.center)
    window.blit(text, text_rect)

def handle_button_eventend(event, button_rect):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):
            return True
    return False