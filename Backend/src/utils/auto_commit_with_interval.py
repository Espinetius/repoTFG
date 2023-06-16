import time
import git


def auto_commit_with_interval(repo_path, commit_message):
    """Realiza commits automáticos en un repositorio con un intervalo de 30 minutos"""
    interval = 30 * 60  # 30 minutos en segundos

    while True:
        try:
            repo = git.Repo(repo_path)
            repo.git.add(all=True)
            repo.git.commit(message=commit_message)
            repo.git.push()

            print(f"Commit realizado: {commit_message}")

            # Esperar 30 minutos antes del próximo commit
            time.sleep(interval)
        except Exception as e:
            print(f"Error al realizar el commit automático: {str(e)}")
