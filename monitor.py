from prometheus_api_client import PrometheusConnect

PROMETHEUS_URL = "http://localhost:9090"
THRESHOLD = 80.0

def check_cpu_spike():
    prom = PrometheusConnect(url=PROMETHEUS_URL, disable_ssl=True)
    query = '100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle"}[2m])) * 100)'
    result = prom.custom_query(query=query)

    for entry in result:
        usage = float(entry["value"][1])
        print(f"CPU Usage: {usage:.2f}%")
        if usage > THRESHOLD:
            return True
    return False

