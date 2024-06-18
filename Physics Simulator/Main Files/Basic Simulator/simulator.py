import pygame
import pymunk
import pymunk.pygame_util
import matplotlib.pyplot as plt

from VTbutton4simulation import create_button, draw_button, handle_button_event
from PTbutton4simulation import create_button1, draw_button1, handle_button_event1
from ATbutton4simulation import create_button2, draw_button2, handle_button_event2
from KEbutton4simulation import create_button3, draw_button3, handle_button_event3
from PEbutton4simulation import create_button4, draw_button4, handle_button_event4
from PEvsKEbutton4simulation import create_button5, draw_button5, handle_button_event5

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 800
GROUND_LEVEL = HEIGHT - 10
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

def draw(space, window, draw_options, button_rect, button1_rect, button2_rect, button3_rect, button4_rect, button5_rect):
    window.fill("white")  # Clear screen with white color
    space.debug_draw(draw_options)
    draw_button(window, button_rect)  # Draw the velocity button
    draw_button1(window, button1_rect)  # Draw the position button
    draw_button2(window, button2_rect)  # Draw the acceleration button
    draw_button3(window, button3_rect)  # Draw the kinetic energy button
    draw_button4(window, button4_rect)  # Draw the potential energy button
    draw_button5(window, button5_rect)  # Draw the KE vs PE button
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
    body.position = (300, 300)  # Initial position of the ball
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 0, 0, 100)  # RGBA: Red with some transparency
    shape.elasticity = 0.7
    space.add(body, shape)
    return body

def plot_velocity_time_graph(times, velocities):
    plt.figure(figsize=(10, 5))
    plt.plot(times, velocities, label='Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (px/s)')
    plt.title('Velocity-Time Graph')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_position_time_graph(times, positions):
    plt.figure(figsize=(10, 5))
    plt.plot(times, positions, label='Position')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (px)')
    plt.title('Position-Time Graph')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_acceleration_time_graph(times, accelerations):
    plt.figure(figsize=(10, 5))
    plt.plot(times, accelerations, label='Acceleration')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (px/s²)')
    plt.title('Acceleration-Time Graph')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_kinetic_energy_time_graph(times, kinetic_energies):
    plt.figure(figsize=(10, 5))
    plt.plot(times, kinetic_energies, label='Kinetic Energy')
    plt.xlabel('Time (s)')
    plt.ylabel('Kinetic Energy (J)')
    plt.title('Kinetic Energy-Time Graph')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_potential_energy_time_graph(times, potential_energies):
    plt.figure(figsize=(10, 5))
    plt.plot(times, potential_energies, label='Potential Energy')
    plt.xlabel('Time (s)')
    plt.ylabel('Potential Energy (J)')
    plt.title('Potential Energy-Time Graph')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_total_energy_time_graph(times, total_energies):
    plt.figure(figsize=(10, 5))
    plt.plot(times, total_energies, label='Total Energy')
    plt.xlabel('Time (s)')
    plt.ylabel('Total Energy (J)')
    plt.title('Total Energy-Time Graph')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_ke_vs_pe_graph(kinetic_energies, potential_energies):
    plt.figure(figsize=(10, 5))
    plt.plot(kinetic_energies, potential_energies, label='KE vs PE', marker='o')
    plt.xlabel('Kinetic Energy (J)')
    plt.ylabel('Potential Energy (J)')
    plt.title('Kinetic Energy vs Potential Energy Graph')
    plt.legend()
    plt.grid(True)
    plt.show()

def run(window, width, height):
    clock = pygame.time.Clock()
    dt = 1 / 144  # Use a smaller time step for more accuracy

    space = pymunk.Space()
    space.gravity = (0, 981)  # Gravity in the y-direction

    create_boundaries(space, width, height)
    ball = create_ball(space, 30, 10)  # Ball with radius 30 and mass 10

    draw_options = pymunk.pygame_util.DrawOptions(window)

    run_simulation = True

    velocities = []
    positions = []
    accelerations = []
    kinetic_energies = []
    potential_energies = []
    total_energies = []
    times = []
    time_elapsed = 0

    button_rect = create_button(window, width, height)
    button1_rect = create_button1(window, width, height)
    button2_rect = create_button2(window, width, height)
    button3_rect = create_button3(window, width, height)
    button4_rect = create_button4(window, width, height)
    button5_rect = create_button5(window, width, height)

    previous_velocity_y = 0

    mass = 10
    gravity = 981

    while run_simulation:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_simulation = False
            elif handle_button_event(event, button_rect):
                run_simulation = False  # Stop the simulation to show the velocity graph
            elif handle_button_event1(event, button1_rect):
                run_simulation = False  # Stop the simulation to show the position graph
            elif handle_button_event2(event, button2_rect):
                run_simulation = False  # Stop the simulation to show the acceleration graph
            elif handle_button_event3(event, button3_rect):
                run_simulation = False  # Stop the simulation to show the kinetic energy graph
            elif handle_button_event4(event, button4_rect):
                run_simulation = False  # Stop the simulation to show the potential energy graph
            elif handle_button_event5(event, button5_rect):
                run_simulation = False  # Stop the simulation to show the KE vs PE graph

        draw(space, window, draw_options, button_rect, button1_rect, button2_rect, button3_rect, button4_rect, button5_rect)
        space.step(dt)

        # Record velocity, position, acceleration, and time
        current_velocity_y = ball.velocity.y  # Y component of velocity
        velocity_change_y = (current_velocity_y - previous_velocity_y) / dt
        velocities.append(current_velocity_y)
        accelerations.append(velocity_change_y)
        positions.append(ball.position.y)  # Y position of the ball
        times.append(time_elapsed)

        # Kinetic Energy: 0.5 * mass * velocity^2
        kinetic_energy = 0.5 * mass * (ball.velocity.length ** 2)
        kinetic_energies.append(kinetic_energy)

        # Potential Energy: mass * gravity * height (height relative to ground)
        height_relative_to_ground = GROUND_LEVEL - ball.position.y
        potential_energy = mass * gravity * height_relative_to_ground
        potential_energies.append(potential_energy)

        # Total Energy
        total_energy = kinetic_energy + potential_energy
        total_energies.append(total_energy)

        time_elapsed += dt

        # Print for debugging purposes
        print(f"Time: {time_elapsed:.2f} s, Velocity: {current_velocity_y:.2f} px/s, Acceleration: {velocity_change_y:.2f} px/s², KE: {kinetic_energy:.2f} J, PE: {potential_energy:.2f} J, Total Energy: {total_energy:.2f} J")

        previous_velocity_y = current_velocity_y

        clock.tick(FPS)

    pygame.quit()

    if handle_button_event(event, button_rect):
        plot_velocity_time_graph(times, velocities)
    elif handle_button_event1(event, button1_rect):
        plot_position_time_graph(times, positions)
    elif handle_button_event2(event, button2_rect):
        plot_acceleration_time_graph(times, accelerations)
    elif handle_button_event3(event, button3_rect):
        plot_kinetic_energy_time_graph(times, kinetic_energies)
    elif handle_button_event4(event, button4_rect):
        plot_potential_energy_time_graph(times, potential_energies)
    elif handle_button_event5(event, button5_rect):
        plot_ke_vs_pe_graph(kinetic_energies, potential_energies)

if __name__ == "__main__":
    run(WINDOW, WIDTH, HEIGHT)
