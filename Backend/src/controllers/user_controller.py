from flask import Blueprint, jsonify, request, current_app, render_template, redirect, url_for
from src.models.User import User

# Crear un objeto Blueprint para el controlador
user_bp = Blueprint('user_controller', __name__)


@user_bp.route('/api/user', methods=['GET'])
def get_all_users():
    try:
        users = User.query_all()
        user_list = [user.to_dict() for user in users]
        return jsonify(user_list)
    except Exception as e:
        print(f"Error retrieving users: {str(e)}")
        return jsonify({'message': 'Failed to retrieve users', 'status': 'error'})


# Ruta para obtener un usuario por nombre de usuario
@user_bp.route('/api/user/<string:username>', methods=['GET'])
def get_user_by_username(username):
    # Llamar al método query_by_username de User para obtener el usuario
    user = User.query_by_username(username)

    if user:
        # Si se encontró el usuario, devolver sus datos en formato JSON
        user_data = {
            '_id': user.id,
            '_name': user.name,
            '_nameuser': user.username,
            '_mail': user.mail
        }
        return jsonify(user_data)
    else:
        # Si no se encontró el usuario, devolver un mensaje de error en formato JSON
        return jsonify({'error': 'Usuario no encontrado'}), 404


# Ruta para obtener un usuario por mail
@user_bp.route('/api/user/<string:mail>', methods=['GET'])
def get_user_by_mail(mail):
    # Llamar al método query_by_username de User para obtener el usuario
    user = User.query_by_mail(mail)

    if user:
        # Si se encontró el usuario, devolver sus datos en formato JSON
        user_data = {
            '_id': user.id,
            '_name': user.name,
            '_nameuser': user.username,
            '_mail': user.mail
        }
        return jsonify(user_data)
    else:
        # Si no se encontró el usuario, devolver un mensaje de error en formato JSON
        return jsonify({'error': 'Mail no encontrado'}), 404


@user_bp.route('/api/user', methods=['POST'])
def create_user():
    try:
        # Obtén los datos del formulario enviado desde el cliente
        new_user_data = request.get_json()

        # Crea una instancia del modelo User con los datos recibidos
        new_user = User(
            id=new_user_data['id'],
            name=new_user_data['name'],
            username=new_user_data['username'],
            mail=new_user_data['mail'],
            password=new_user_data['password']
        )

        # Guarda el usuario en la base de datos
        if new_user.save():
            return jsonify({'message': 'Usuario creado correctamente'})
        else:
            return jsonify({'error': 'Error al crear el usuario'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        # Obtener los datos del usuario desde el formulario de Vue
        user_data = request.get_json()

        # Crea una instancia del modelo User con los datos recibidos
        user = User(
            id=user_id,
            name=user_data['name'],
            username=user_data['username'],
            mail=user_data['mail'],
            password=user_data['password']
        )

        # Actualiza el usuario en la base de datos
        if user.update():
            return jsonify({'message': 'Usuario actualizado exitosamente'})
        else:
            return jsonify({'message': 'Error al actualizar el usuario'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        # Elimina el usuario de la base de datos
        if User.delete(user_id):
            return jsonify({'message': 'Usuario eliminado exitosamente'})
        else:
            return jsonify({'message': 'Error al eliminar el usuario'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Ruta para iniciar sesión
@user_bp.route('/api/user/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        mail = data['mail']
        password = data['password']
        print(mail)
        print(password)
        if User.login(mail, password):
            print(f'redireccionando a indexuser')
            return redirect(url_for('indexuser'))
        else:
            return render_template('login.html', error_message='Credenciales inválidas')
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Método para registrar un nuevo usuario en MongoDB
@user_bp.route('/api/user/register', methods=['POST'])
def register_user():
    try:
        # Obtén los datos del formulario enviado desde el cliente
        new_user_data = request.get_json()

        # Establecer la conexión con la base de datos MongoDB
        client = MongoClient(Config.MONGODB_HOST, Config.MONGODB_PORT)
        db = client[Config.MONGODB_DATABASE]
        collection = db['users']

        # Crear el documento del usuario a insertar en la base de datos
        user = {
            '_name': new_user_data['name'],
            '_username': new_user_data['username'],
            '_mail': new_user_data['mail'],
            '_password': new_user_data['password']
        }

        # Insertar el documento en la colección de usuarios
        result = collection.insert_one(user)

        # Cerrar la conexión con la base de datos
        client.close()

        # Redirigir al usuario al template indexuser.html
        return redirect('/indexuser.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

