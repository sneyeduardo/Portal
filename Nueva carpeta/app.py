import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Tu función matemática exacta del archivo fourier.py
def fourier_square_wave(t, num_harmonics):
    square_wave_approx = np.zeros_like(t, dtype=float)
    for i in range(1, 2 * num_harmonics, 2):
        square_wave_approx += (1 / i) * np.sin(i * t)
    return (4 / np.pi) * square_wave_approx

# Ruta principal que muestra el HTML
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint de API que calcula todos los frames para la animación
@app.route('/api/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    max_harmonics = int(data.get('harmonics', 10))
    
    # Limitar por seguridad para no sobrecargar el servidor gratuito
    max_harmonics = max(1, min(max_harmonics, 100))
    
    # Mismo rango de tiempo de tu script original
    t = np.linspace(-np.pi * 2, np.pi * 2, 500)
    
    # Generamos cada cuadro (frame) desde 1 hasta max_harmonics
    frames = []
    for n in range(1, max_harmonics + 1):
        y_approx = fourier_square_wave(t, n)
        frames.append({
            'harmonic': n,
            'y': y_approx.tolist()
        })
        
    return jsonify({
        't': t.tolist(),
        'frames': frames
    })

if __name__ == '__main__':
    app.run(debug=True)