import os


class Config:
    # Configuración de la base de datos MongoDB
    MONGODB_HOST = os.getenv('MONGODB_HOST', 'mongodb+srv://dandelionrepos:tfgDAW@dandelionusers.ptuwecg.mongodb.net/')
    MONGODB_PORT = int(os.getenv('MONGODB_PORT', 27017))
    MONGODB_DATABASE = os.getenv('MONGODB_DATABASE', 'dandelion')

    # Configuracion de la base de datos en el contenedor
    DB_HOST = os.getenv('DB_HOST', '172.17.0.2')
    DB_PORT = int(os.getenv('DB_PORT', 2000))
    DB_USER = os.getenv('DB_USER', 'dandelion-sql-server')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'dandelion1234')

    # Configuración del repositorio en Docker
    DOCKER_REPO_PATH = os.getenv('DOCKER_REPO_PATH', './dockerfile.txt')


DOCKER_REPO_PATH = Config.DOCKER_REPO_PATH
