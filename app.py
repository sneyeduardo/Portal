import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Configuración de la página web
st.title("🌊 Animación de Onda Cuadrada con Series de Fourier")
st.write("Ajusta el número máximo de armónicos impares para ver cómo la suma de senos se aproxima a una onda cuadrada.")

# Control deslizante (slider) para que el usuario elija el número de armónicos
max_harmonics = st.slider("Número de Armónicos Impares", min_value=1, max_value=30, value=10, step=1)

def fourier_square_wave(t, num_harmonics):
    square_wave_approx = np.zeros_like(t, dtype=float)
    # Consideramos únicamente armónicos impares
    for i in range(1, 2 * num_harmonics, 2):
        square_wave_approx += (1 / i) * np.sin(i * t)
    return (4 / np.pi) * square_wave_approx

# Definir el rango de tiempo (dos ciclos de la onda)
t = np.linspace(-np.pi * 2, np.pi * 2, 500)

# Crear la gráfica estática de Matplotlib usando el valor seleccionado por el usuario
fig, ax = plt.subplots(figsize=(10, 5))

# Dibujar las curvas de los armónicos individuales o la suma total
y_approx = fourier_square_wave(t, max_harmonics)

ax.plot(t, y_approx, label=f'Aproximación ({max_harmonics} armónicos)', color='blue', linewidth=2)

# Referencia de la onda cuadrada ideal para comparar
ideal_wave = np.sign(np.sin(t))
ax.plot(t, ideal_wave, label='Onda Cuadrada Ideal', color='red', linestyle='--', alpha=0.5)

ax.set_title(f'Aproximación con {max_harmonics} Armónico(s) Impar(es)')
ax.set_xlabel('Tiempo (t)')
ax.set_ylabel('Amplitud')
ax.grid(True)
ax.set_ylim(-1.5, 1.5)
ax.legend()

# Mostrar la gráfica interactiva en Streamlit
st.pyplot(fig)