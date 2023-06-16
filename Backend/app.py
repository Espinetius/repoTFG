from flask import Flask, render_template, jsonify, redirect, request, url_for
from config import Config
from src.controllers.user_controller import user_bp, register_user, login_user
from src.controllers.git_controller import git_bp

# Crear la aplicación Flask
app = Flask(__name__, static_folder='static')
app.config.from_object(Config)

# Registrar el Blueprint del controlador de usuario y git
app.register_blueprint(user_bp)
app.register_blueprint(git_bp)

# Redireccionar la URL raíz '/' a '/login'
@app.route('/')
def root():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Llama a la función del controlador para iniciar sesión
        if login_user():
            # Aquí puedes redirigir al usuario a la página deseada después del inicio de sesión
            return redirect(url_for('indexuser'))
        else:
            return None

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Procesar los datos del formulario de registro
        name = request.form['name']
        username = request.form['username']
        mail = request.form['mail']
        password = request.form['password']

        # Llama a la función del controlador para dar de alta al usuario
        register_user(name, username, mail, password)

        # Redirige al usuario a la página de inicio o a la página deseada después del registro
        return redirect(url_for('indexuser'))

    return render_template('register.html')

@app.route('/indexuser', methods=['GET'])
def indexuser():
    print(f'redireccionado')
    return render_template('indexuser.html')

@app.route('/userconfig', methods=['GET'])
def userconfig():
    return render_template('userconfig.html')

@app.route('/userrepo', methods=['GET'])
def userrepo():
    return render_template('userrepo.html')

# Configurar Flask para manejar solicitudes JSON
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

if __name__ == '__main__':
    app.run()
