import datetime

def log_event(container_name, analysis, action_result):
    with open("agent.log", "a") as f:
        f.write(f"""
🕒 {datetime.datetime.now()}
🔍 Container: {container_name}
🧠 Analysis: {analysis}
🔁 Action: {action_result}
-------------------------------
""")
