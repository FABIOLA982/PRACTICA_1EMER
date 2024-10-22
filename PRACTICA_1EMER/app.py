from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de "Quiénes Somos"
@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

# Ruta para la página de "Servicios"
@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

# Ruta para la página de "Noticias"
@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

# Ruta para la página de "Contacto"
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        # Aquí puedes manejar el envío de los datos como desees
        # Por ejemplo, puedes guardarlos en una base de datos o enviarlos por correo
        return redirect(url_for('gracias'))
    return render_template('contacto.html')

# Ruta de agradecimiento después de enviar el formulario
@app.route('/gracias')
def gracias():
    return "Gracias por tu mensaje. Nos pondremos en contacto contigo pronto."

if __name__ == '__main__':
    app.run(debug=True)