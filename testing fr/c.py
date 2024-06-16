import pygame
import pymunk
import pymunk.pygame_util
import matplotlib.pyplot as plt
from a import create_button, draw_button, handle_button_event


pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60


button_pressed = False
simulation_running = True

def draw(space, window, draw_options, button_rect):
    window.fill("white")  
    space.debug_draw(draw_options)
    draw_button(window, button_rect)  
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
        shape.elasticity = 0.7  
        space.add(body, shape)

def create_ball(space, radius, mass):
    body = pymunk.Body()
    body.position = (300, 300)  
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 0, 0, 100)  
    shape.elasticity = 0.7  # Adding some bounce to the ball
    space.add(body, shape)
    return body

def initialize_plot():
    plt.ion()  
    fig, ax = plt.subplots(figsize=(10, 5))
    line, = ax.plot([], [], label='Velocity')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Velocity (m/s)')
    ax.set_title('Velocity-Time Graph')
    ax.legend()
    ax.grid(True)
    return fig, ax, line

def update_plot(fig, ax, line, times, velocities):
    line.set_data(times, velocities)
    ax.relim()
    ax.autoscale_view(True, True, True)
    fig.canvas.flush_events()
    plt.pause(0.001)  # Pause to update the plot

def run(window, width, height):
    global simulation_running, button_pressed
    dt = 1 / FPS

    space = pymunk.Space()
    space.gravity = (0, 981)  # Gravity in the y-direction

    create_boundaries(space, width, height)
    ball = create_ball(space, 30, 10)  

    draw_options = pymunk.pygame_util.DrawOptions(window)
    button_rect = create_button(window, width, height)

    clock = pygame.time.Clock()
    time_elapsed = 0
    velocities = []
    times = []

    fig, ax, line = None, None, None

    print("Starting main loop")
    while simulation_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                simulation_running = False
            elif handle_button_event(event, button_rect):
                button_pressed = True  # Signal that the button was pressed
                if fig is None:
                    fig, ax, line = initialize_plot()  # Initialize plot only once

        space.step(dt)

        # Record velocity and time
        if len(space.bodies) > 1:
            ball = space.bodies[1]  
            velocity = ball.velocity.length  
            velocities.append(velocity)
            times.append(time_elapsed)
            time_elapsed += dt

        draw(space, window, draw_options, button_rect)  

        if button_pressed:
            update_plot(fig, ax, line, times, velocities) 

        clock.tick(FPS)

    print("Ending main loop")
    pygame.quit()
    plt.close()

if __name__ == "__main__":
    run(WINDOW, WIDTH, HEIGHT)
