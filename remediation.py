import subprocess

def restart_container(container_name):
    try:
        subprocess.run(["docker", "restart", container_name], check=True)
        return f" Container '{container_name}' restarted successfully."
    except subprocess.CalledProcessError as e:
        return f" Failed to restart container '{container_name}': {e}"
