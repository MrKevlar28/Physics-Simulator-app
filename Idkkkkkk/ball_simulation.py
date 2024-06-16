import pygame
import pymunk
import pymunk.pygame_util
import matplotlib.pyplot as plt
import sys
from button import create_button, draw_button, handle_button_event

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

def draw(space, window, draw_options, button_rect):
    window.fill("white")  # Clear screen with white color
    space.debug_draw(draw_options)
    draw_button(window, button_rect)  # Draw the button
    pygame.display.update()

def create_boundaries(space, width, height):
    rects = [
        # Floor
        [(width / 2, height - 10), (width, 20)],
        # Ceiling
        [(width / 2, 10), (width, 20)],
        # Walls
        [(10, height / 2), (20, height)],
        [(width - 10, height / 2), (20, height)],
    ]
    
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.7  # Adding some bounce to the boundaries
        space.add(body, shape)

def create_ball(space, radius, mass):
    body = pymunk.Body()
    body.position = (300, 300)  # Initial position of the ball
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 0, 0, 100)  # RGBA: Red with some transparency
    shape.elasticity = 0.7  # Adding some bounce to the ball
    space.add(body, shape)
    return body

def plot_velocity_time_graph(times, velocities):
    plt.figure(figsize=(10, 5))
    plt.plot(times, velocities, label='Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity-Time Graph')
    plt.legend()
    plt.grid(True)
    plt.show()

def run(window, width, height):
    clock = pygame.time.Clock()
    dt = 1 / FPS

    space = pymunk.Space()
    space.gravity = (0, 981)  # Gravity in the y-direction

    create_boundaries(space, width, height)
    ball = create_ball(space, 30, 10)  # Ball with radius 30 and mass 10

    draw_options = pymunk.pygame_util.DrawOptions(window)

    run_simulation = True

    velocities = []
    times = []
    time_elapsed = 0

    button_rect = create_button(window, width, height)

    while run_simulation:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_simulation = False
            elif handle_button_event(event, button_rect):
                run_simulation = False  # Stop the simulation to show the graph

        draw(space, window, draw_options, button_rect)
        space.step(dt)

        # Record velocity and time
        velocity = ball.velocity.length  # Magnitude of velocity
        velocities.append(velocity)
        times.append(time_elapsed)
        time_elapsed += dt

        clock.tick(FPS)

    pygame.quit()

    # Plotting the velocity-time graph using Matplotlib
    plot_velocity_time_graph(times, velocities)

if __name__ == "__main__":
    run(WINDOW, WIDTH, HEIGHT)
