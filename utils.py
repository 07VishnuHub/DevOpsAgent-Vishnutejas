import subprocess

def get_highest_cpu_container():
    try:
        output = subprocess.check_output([
            "docker", "stats", "--no-stream", "--format",
            "{{.Name}}:{{.CPUPerc}}"
        ]).decode()

        max_cpu = 0
        top_container = None

        for line in output.splitlines():
            try:
                name, cpu = line.split(":")
                cpu_val = float(cpu.strip().replace("%", ""))
                if cpu_val > max_cpu:
                    max_cpu = cpu_val
                    top_container = name.strip()
            except:
                continue

        return top_container, max_cpu

    except Exception as e:
        print(f" Error fetching container stats: {e}")
        return None, 0
