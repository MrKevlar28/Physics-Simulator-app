import threading
import pygame
import pymunk
import pymunk.pygame_util
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from VTbutton4simulation import create_button, draw_button, handle_button_event
from PTbutton4simulation import create_button1, draw_button1, handle_button_event1
from ATbutton4simulation import create_button2, draw_button2, handle_button_event2
from KEbutton4simulation import create_button3, draw_button3, handle_button_event3
from PEbutton4simulation import create_button4, draw_button4, handle_button_event4
from PEvsKEbutton4simulation import create_button5, draw_button5, handle_button_event5
from Endbutton import create_Endbutton, draw_Endbutton, handle_button_eventend

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 800
GROUND_LEVEL = HEIGHT - 10
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60  # Adjust FPS for better performance
DT = 1 / 60  # Adjust dt for smoother simulation

# Shared data lists
time_data = []
velocity_data = []
position_data = []
acceleration_data = []
kinetic_energy_data = []
potential_energy_data = []

def draw(space, window, draw_options, button_rect, button1_rect, button2_rect, button3_rect, button4_rect, button5_rect, Endbutton_rect):
    window.fill("white")  # Clear screen with white color
    space.debug_draw(draw_options)
    draw_button(window, button_rect)  # Draw the velocity button
    draw_button1(window, button1_rect)  # Draw the position button
    draw_button2(window, button2_rect)  # Draw the acceleration button
    draw_button3(window, button3_rect)  # Draw the kinetic energy button
    draw_button4(window, button4_rect)  # Draw the potential energy button
    draw_button5(window, button5_rect)  # Draw the KE vs PE button
    draw_Endbutton(window,Endbutton_rect) # Draw End button
    
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

def update_plot(ax, x_data, y_data, title, xlabel, ylabel):
    ax.clear()
    ax.plot(x_data, y_data)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)

def create_plot_window(title, xlabel, ylabel, x_data, y_data):
    plot_window = tk.Toplevel()
    plot_window.title(title)
    fig, ax = plt.subplots(figsize=(8, 6))
    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_plot_wrapper():
        update_plot(ax, x_data, y_data, title, xlabel, ylabel)
        canvas.draw()
        plot_window.after(1000, update_plot_wrapper)  # Update every 1 second to reduce lag

    update_plot_wrapper()

def run_simulation(window, width, height):
    clock = pygame.time.Clock()
    dt = DT

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
    Endbutton_rect = create_Endbutton(window,width,height)

    previous_velocity_y = 0

    mass = 10
    gravity = 981

    def handle_events():
        nonlocal run_simulation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_simulation = False
            elif handle_button_event(event, button_rect):
                create_plot_window("Velocity-Time Graph", "Time (s)", "Velocity (px/s)", times, velocities)
            elif handle_button_event1(event, button1_rect):
                create_plot_window("Position-Time Graph", "Time (s)", "Position (px)", times, positions)
            elif handle_button_event2(event, button2_rect):
                create_plot_window("Acceleration-Time Graph", "Time (s)", "Acceleration (px/s²)", times, accelerations)
            elif handle_button_event3(event, button3_rect):
                create_plot_window("Kinetic Energy-Time Graph", "Time (s)", "Kinetic Energy (J)", times, kinetic_energies)
            elif handle_button_event4(event, button4_rect):
                create_plot_window("Potential Energy-Time Graph", "Time (s)", "Potential Energy (J)", times, potential_energies)
            elif handle_button_event5(event, button5_rect):
                create_plot_window("Kinetic Energy vs Potential Energy Graph", "Kinetic Energy (J)", "Potential Energy (J)", kinetic_energies, potential_energies)
            elif handle_button_eventend(event, Endbutton_rect):        
                run_simulation = False

    while run_simulation:
        handle_events()
        draw(space, window, draw_options, button_rect, button1_rect, button2_rect, button3_rect, button4_rect, button5_rect, Endbutton_rect)
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

        # Update plot data
        time_data.append(time_elapsed)
        velocity_data.append(current_velocity_y)
        position_data.append(ball.position.y)
        acceleration_data.append(velocity_change_y)
        kinetic_energy_data.append(kinetic_energy)
        potential_energy_data.append(potential_energy)

        previous_velocity_y = current_velocity_y
        clock.tick(FPS)
    
    pygame.quit()

def start_simulation():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    simulation_thread = threading.Thread(target=run_simulation, args=(WINDOW, WIDTH, HEIGHT))
    simulation_thread.start()
    root.mainloop()
    simulation_thread.join()

if __name__ == "__main__":
    start_simulation()
