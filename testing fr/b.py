import matplotlib.pyplot as plt

def plot_velocity_time_graph(times, velocities):
    plt.figure(figsize=(10, 5))
    plt.plot(times, velocities, label='Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity-Time Graph')
    plt.legend()
    plt.grid(True)
    plt.show()
