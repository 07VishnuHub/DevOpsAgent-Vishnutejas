from monitor import check_cpu_spike
from langchain_agent import run_devops_langchain_agent

if check_cpu_spike():
    print(" CPU spike detected. Running LangChain agent...")
    result = run_devops_langchain_agent()
    print("\n Final Result:\n", result)
else:
    print(" CPU usage normal.")

