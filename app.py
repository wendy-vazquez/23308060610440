from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'clave_secreta_y_muy_larga'

@app.route('/')
def index():
    return redirect('/form')

@app.route('/form', methods=['GET', 'POST'])
def formulario():
    if 'alimentos_clasificados' not in session:
        session['alimentos_clasificados'] = []

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        grasas = float(request.form.get('grasas'))
        proteinas = float(request.form.get('proteinas'))
        carbohidratos = float(request.form.get('carbohidratos', 0))

        g_cal = grasas * 9
        p_cal = proteinas * 4
        c_cal = carbohidratos * 4

        tipo = max(
            {'Grasas': g_cal, 'Proteínas': p_cal, 'Carbohidratos': c_cal},
            key=lambda x: {'Grasas': g_cal, 'Proteínas': p_cal, 'Carbohidratos': c_cal}[x]
        )
        resultado = f'Fuente de {tipo}'

        session['alimentos_clasificados'].append({'nombre': nombre, 'clasificacion': resultado})
        session.modified = True  # Necesario para que Flask registre el cambio en la sesión

    return render_template('formulario.html', alimentos=session['alimentos_clasificados'])

@app.route('/limpiar_lista', methods=['POST'])
def limpiar_lista():
    session['alimentos_clasificados'] = []
    session.modified = True
    return redirect('/form')

if __name__ == '__main__':
    app.run(debug=True)