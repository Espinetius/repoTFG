import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import current_app, request, jsonify
from config import Config


class User:
    def __init__(self, id, name, username, mail, password):
        self.id = id
        self.name = name
        self.username = username
        self.mail = mail
        self.password = password

    def save(self):
        try:
            # Obtener la configuración de la base de datos desde current_app
            mongo_host = current_app.config['MONGODB_HOST']
            mongo_port = current_app.config['MONGODB_PORT']
            mongo_database = current_app.config['MONGODB_DATABASE']

            # Conectar a la base de datos
            client = MongoClient(mongo_host, mongo_port)
            db = client[mongo_database]

            # Insertar el usuario en la colección
            user_data = {
                '_id': self.id,
                '_name': self.name,
                '_nameuser': self.username,
                '_mail': self.mail,
                '_password': self.password
            }
            print(f"user_data: {user_data}")
            result = db.users.insert_one(user_data)

            # Verificar si la inserción fue exitosa
            if result.inserted_id:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error saving user: {str(e)}")
            return False

    def update(self):
        try:
            # Obtener la configuración de la base de datos desde current_app
            mongo_host = current_app.config['MONGODB_HOST']
            mongo_port = current_app.config['MONGODB_PORT']
            mongo_database = current_app.config['MONGODB_DATABASE']

            # Conectar a la base de datos
            client = MongoClient(mongo_host, mongo_port)
            db = client[mongo_database]

            # Actualizar el usuario en la colección
            user_data = {
                '_name': self.name,
                '_nameuser': self.username,
                '_mail': self.mail,
                '_password': self.password
            }
            result = db.users.update_one({'_id': ObjectId(self.id)}, {'$set': user_data})

            # Verificar si la actualización fue exitosa
            if result.modified_count > 0:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error updating user: {str(e)}")
            return False

    @staticmethod
    def delete(user_id):
        try:
            # Obtener la configuración de la base de datos desde current_app
            mongo_host = current_app.config['MONGODB_HOST']
            mongo_port = current_app.config['MONGODB_PORT']
            mongo_database = current_app.config['MONGODB_DATABASE']

            # Conectar a la base de datos
            client = MongoClient(mongo_host, mongo_port)
            db = client[mongo_database]

            # Eliminar el usuario de la colección
            result = db.users.delete_one({'_id': ObjectId(user_id)})

            # Verificar si la eliminación fue exitosa
            if result.deleted_count > 0:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error deleting user: {str(e)}")
            return False

    @staticmethod
    def query_all():
        try:
            # Obtener la configuración de la base de datos desde current_app
            mongo_host = current_app.config['MONGODB_HOST']
            mongo_port = current_app.config['MONGODB_PORT']
            mongo_database = current_app.config['MONGODB_DATABASE']

            # Conectar a la base de datos
            client = MongoClient(mongo_host, mongo_port)
            db = client[mongo_database]

            # Consultar todos los usuarios de la colección
            users = db.users.find()

            # Crear una lista de objetos User a partir de los resultados de la consulta
            user_list = [User(
                str(user['_id']),
                user['_name'],
                user['_nameuser'],
                user['_mail'],
                user['_password']
            ) for user in users]

            return user_list
        except Exception as e:
            print(f"Error querying users: {str(e)}")
            return []

    @staticmethod
    def query_by_username(username):
        try:
            # Obtener la configuración de la base de datos desde current_app
            mongo_host = current_app.config['MONGODB_HOST']
            mongo_port = current_app.config['MONGODB_PORT']
            mongo_database = current_app.config['MONGODB_DATABASE']

            # Conectar a la base de datos
            client = MongoClient(mongo_host, mongo_port)
            db = client[mongo_database]

            # Consultar un usuario por su nombre de usuario en la colección
            user = db.users.find_one({'_nameuser': username})

            # Verificar si se encontró el usuario
            if user:
                return User(
                    str(user['_id']),
                    user['_name'],
                    user['_nameuser'],
                    user['_mail'],
                    user['_password']
                )
            else:
                return None
        except Exception as e:
            print(f"Error querying user by username: {str(e)}")
            return None

    @staticmethod
    def query_by_mail(mail):
        try:
            # Obtener la configuración de la base de datos desde current_app
            mongo_host = current_app.config['MONGODB_HOST']
            mongo_port = current_app.config['MONGODB_PORT']
            mongo_database = current_app.config['MONGODB_DATABASE']

            # Conectar a la base de datos
            client = MongoClient(mongo_host, mongo_port)
            db = client[mongo_database]

            # Consultar un usuario por su nombre de usuario en la colección
            user = db.users.find_one({'_mail': mail})

            # Verificar si se encontró el usuario
            if user:
                return User(
                    str(user['_id']),
                    user['_name'],
                    user['_nameuser'],
                    user['_mail'],
                    user['_password']
                )
            else:
                return None
        except Exception as e:
            print(f"Error querying user by mail: {str(e)}")
            return None

    @staticmethod
    def login(mail, password):
        try:
            # Obtener el usuario por mail desde la base de datos
            user = User.query_by_mail(mail)
            if user and User.authenticate(user.mail, password):
                print(f'logeado')
                return user
            print(f'no logeado')
            return None
        except Exception as e:
            print(f"Error during login: {str(e)}")
            return None

    @staticmethod
    def authenticate(mail, password):
        try:
            # Obtener la configuración de la base de datos desde current_app
            mongo_host = current_app.config['MONGODB_HOST']
            mongo_port = current_app.config['MONGODB_PORT']
            mongo_database = current_app.config['MONGODB_DATABASE']

            # Conectar a la base de datos
            client = MongoClient(mongo_host, mongo_port)
            db = client[mongo_database]

            # Consultar el usuario por correo electrónico
            user = db.users.find_one({'_mail': mail})

            # Verificar si se encontró el usuario y si la contraseña coincide
            if user and user['_password'] == password:
                print(f'autenticado')
                return True
            else:
                print(f'no autenticado')
                return False
        except Exception as e:
            print(f"Error authenticating user: {str(e)}")
            return False

    @classmethod
    def exists(cls, mail):
        user = cls.query_by_mail(mail)
        return user is not None

    def to_dict(self):
        return {
            '_id': self.id,
            '_name': self.name,
            '_nameuser': self.username,
            '_mail': self.mail,
            '_password': self.password
        }
