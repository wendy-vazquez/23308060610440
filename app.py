from flask import Flask, request, render_template

app = '__name__'

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/form', methods=['GET', 'POST'])
def formulario():
    return render_template('formulario.html')

@app.route('/resu')
def resultado():
    return render_template('resultado.html')

if __name__ == '__main__':
    app.run(debug=True)