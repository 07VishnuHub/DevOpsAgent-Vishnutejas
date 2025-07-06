from langchain.agents import Tool, initialize_agent
from langchain_community.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
import os
import datetime

# Load env
load_dotenv()

# Import your functions
from monitor import check_cpu_spike
from utils import get_highest_cpu_container
from fetch_logs import get_docker_logs
from llm_analysis import analyze_logs
from remediation import restart_container
from notifier import send_email
from log_action import log_event

# Track state (global) — this makes it easier inside tool functions
STATE = {
    "container": None,
    "cpu": 0,
    "logs": "",
    "analysis": "",
    "action": ""
}

# Tool: Identify container with highest CPU
def detect_top_container(_):
    name, cpu = get_highest_cpu_container()
    STATE["container"] = name
    STATE["cpu"] = cpu
    return f" Container: {name}, CPU Usage: {cpu}%"

# Tool: Fetch logs
def fetch_logs(_):
    if not STATE["container"]:
        return " No container selected."
    logs = get_docker_logs(STATE["container"])
    STATE["logs"] = logs
    return logs[:1000] or "No logs found."

# Tool: Analyze logs
def analyze_logs_llm(_):
    if not STATE["logs"].strip():
        return "No logs to analyze."
    result = analyze_logs(STATE["logs"])
    STATE["analysis"] = result
    return result

# Tool: Remediation (restart container)
def restart_if_needed(_):
    if "restart" in STATE["analysis"].lower() or "cpu" in STATE["analysis"].lower():
        result = restart_container(STATE["container"])
        STATE["action"] = result
    else:
        result = "Restart not needed — LLM didn’t suggest."
        STATE["action"] = result
    return result

# Tool: Notify
def send_notification(_):
    subject = f"DevOps AI Alert: {STATE['container']}"
    msg = f"""
 {datetime.datetime.now()}
 Container: {STATE['container']}
 CPU: {STATE['cpu']}%
 LLM Analysis: {STATE['analysis']}
 Action Taken: {STATE['action']}
"""
    send_email(subject, msg)
    log_event(STATE["container"], STATE["analysis"], STATE["action"])
    return "✅ Notification sent + action logged."

# Register tools
tools = [
    Tool(name="DetectTopContainer", func=detect_top_container, description="Detect the container with highest CPU usage"),
    Tool(name="FetchLogs", func=fetch_logs, description="Fetch logs from the top container"),
    Tool(name="AnalyzeLogs", func=analyze_logs_llm, description="Use LLM to analyze logs and find CPU cause"),
    Tool(name="RestartContainer", func=restart_if_needed, description="Restart container if needed"),
    Tool(name="NotifyTeam", func=send_notification, description="Send email and log the incident")
]

# Run the LangChain agent
def run_devops_langchain_agent():
    llm = ChatOpenAI(model="gpt-4", temperature=0.3)
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent.run("There is a CPU spike. Investigate which container is the cause and take appropriate action.")
