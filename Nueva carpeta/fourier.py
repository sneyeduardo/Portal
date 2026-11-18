import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def fourier_square_wave(t, num_harmonics):
    square_wave_approx = np.zeros_like(t, dtype=float)
    for i in range(1, 2 * num_harmonics, 2):
        square_wave_approx += (1 / i) * np.sin(i * t)
    return (4 / np.pi) * square_wave_approx

def generar_animacion():
    t = np.linspace(-np.pi * 2, np.pi * 2, 500)
    fig, ax = plt.subplots(figsize=(10, 6))
    line, = ax.plot(t, np.zeros_like(t), label='Aproximación de Onda Cuadrada', color='blue')
    ax.set_title('Aproximación de Onda Cuadrada con Series de Fourier')
    ax.set_xlabel('Tiempo (t)')
    ax.set_ylabel('Amplitud')
    ax.grid(True)
    ax.set_ylim(-1.5, 1.5)

    def update(num_harmonics_so_far):
        y_approx = fourier_square_wave(t, num_harmonics_so_far)
        line.set_ydata(y_approx)
        ax.set_title(f'Aproximación con {num_harmonics_so_far} Armónico(s)')
        return line,

    # Generamos la animación con 15 armónicos máximos
    ani = FuncAnimation(fig, update, frames=range(1, 16), interval=200, blit=True)

    # En lugar de plt.show(), guardamos la animación como GIF para el servidor
    ani.save("fourier_wave.gif", writer='pillow')
    print("¡Animación guardada con éxito como fourier_wave.gif!")

if __name__ == '__main__':
    generar_animacion()