from flask import Blueprint, jsonify, request, current_app
import git
from src.models.repository import Repository
from config import DOCKER_REPO_PATH
from flask_restful import Resource
from config import Config

# Crear el controlador (Blueprint)
git_bp = Blueprint('git_controller', __name__)

DOCKER_REPO_PATH = Config.DOCKER_REPO_PATH


class RepoList(Resource):
    def get(self):
        try:
            # Obtener la lista de repositorios desde tu fuente de datos (por ejemplo, una API de Git)
            repositories = GitAPI.get_repositories()

            # Crear una lista para almacenar los nombres de los repositorios
            repo_names = []

            # Iterar sobre los repositorios y agregar sus nombres a la lista
            for repo in repositories:
                repo_names.append(repo.name)

            # Devolver la lista de nombres de repositorios en formato JSON
            return jsonify(repo_names)
        except Exception as e:
            return jsonify({'error': str(e)}), 500


# Ruta para hacer un pull desde el repositorio
@git_bp.route('/api/git/pull', methods=['GET'])
def git_pull():
    try:
        repo = git.Repo(DOCKER_REPO_PATH)
        repo.pull()
        return jsonify({'message': 'Pull realizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Ruta para hacer un push al repositorio
@git_bp.route('/api/git/push', methods=['GET'])
def git_push():
    try:
        repo = git.Repo(DOCKER_REPO_PATH)
        repo.push()
        return jsonify({'message': 'Push realizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Ruta para hacer un commit en el repositorio
@git_bp.route('/api/git/commit', methods=['POST'])
def git_commit():
    try:
        repo = git.Repo(DOCKER_REPO_PATH)
        commit_message = request.form.get('message')
        repo.git.commit(message=commit_message)
        return jsonify({'message': 'Commit realizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Ruta para hacer un merge request en el repositorio
@git_bp.route('/api/git/merge', methods=['POST'])
def git_merge():
    try:
        repo = git.Repo(DOCKER_REPO_PATH)
        source_branch = request.form.get('source_branch')
        target_branch = request.form.get('target_branch')
        repo.git.merge_request(source_branch, target_branch)
        return jsonify({'message': 'Merge request realizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Ruta para mostrar la tabla del usuario en el repositorio
@git_bp.route('/api/git/<string:username>_table', methods=['GET'])
def show_user_table(username):
    try:
        # Verifica si el usuario existe en el repositorio
        if repository.check_user_table(username):
            # Obtiene los datos de la tabla del usuario desde el repositorio
            user_table_data = repository.get_user_table_data(username)

            # Realiza cualquier procesamiento adicional necesario
            for row in user_table_data:
                # Agregar URL de previsualización del archivo
                file_path = row['file_path']
                preview_url = f"/api/git/preview?file_path={file_path}"
                row['preview_url'] = preview_url

                # Agregar URL de eliminación del archivo
                delete_url = f"/api/git/delete?file_path={file_path}"
                row['delete_url'] = delete_url

                # Agregar URL de descarga del archivo
                download_url = f"/api/git/download?file_path={file_path}"
                row['download_url'] = download_url

            # Devuelve la respuesta en formato JSON
            return jsonify(user_table_data)
        else:
            return jsonify({'error': 'Ups, parece que ha habido un problema con la tabla ...'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
