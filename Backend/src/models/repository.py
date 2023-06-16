import docker
from threading import Thread
from config import DOCKER_REPO_PATH
from src.utils.auto_commit_with_interval import auto_commit_with_interval
from flask import current_app
from config import Config

DOCKER_REPO_PATH = Config.DOCKER_REPO_PATH


class Repository:
    @staticmethod
    def start_container():
        # Iniciar un contenedor Docker a partir de una imagen
        try:
            client = docker.from_env()
            container = client.containers.run(DOCKER_REPO_PATH, detach=True)
            return container.id
        except docker.errors.APIError as e:
            print(f"Error starting container: {str(e)}")
            return None

    @staticmethod
    def stop_container(container_id):
        # Detener y eliminar un contenedor Docker
        try:
            client = docker.from_env()
            container = client.containers.get(container_id)
            container.stop()
            container.remove()
            return True
        except docker.errors.NotFound:
            return False
        except docker.errors.APIError as e:
            print(f"Error stopping container: {str(e)}")
            return False

    @staticmethod
    def auto_commit_callback():
        auto_commit_with_interval(DOCKER_REPO_PATH, "Automatic commit message")

    @staticmethod
    def start_auto_commit():
        auto_commit_thread = Thread(target=Repository.auto_commit_callback)
        auto_commit_thread.start()


