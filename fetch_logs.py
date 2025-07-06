import subprocess

def get_docker_logs(container_name, minutes=5):
    try:
        logs = subprocess.check_output([
            "docker", "logs", f"--since={minutes}m", container_name
        ])
        return logs.decode()
    except Exception as e:
        return f" Could not fetch logs: {e}"
