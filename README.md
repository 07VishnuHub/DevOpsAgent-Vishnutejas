# DevOpsAgent-Vishnutejas
# 🤖 DevOps AI Agent

An AI-powered, autonomous DevOps agent that monitors your infrastructure in real-time, detects CPU anomalies, analyzes logs using GPT-4, performs intelligent remediation by restarting Docker containers, and notifies your team with a detailed report.

---

## 🧠 Key Features

- ✅ Monitors CPU usage using Prometheus + Node Exporter  
- 📦 Dynamically detects the Docker container consuming the most CPU  
- 📜 Fetches real-time logs from the top container  
- 🧠 Analyzes logs using GPT-4 (via OpenAI + LangChain)  
- 🔁 Automatically restarts the container if the LLM suggests it  
- 📬 Sends a detailed summary via email (Gmail SMTP)  
- 📝 Logs all actions locally for auditing and debugging  

---

## 🛠 Tech Stack

- Python 3.10
- Prometheus (Node Exporter)
- Docker (Container monitoring)
- OpenAI GPT-4 + LangChain
- SMTP (Gmail)
- Crontab (optional for automation)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone repo
cd devops-ai-agent
```
### Install Requirements
```bash
pip install -r requirements.txt
```

### Configure .env
OPENAI_API_KEY=sk-...
SMTP_USER=your@gmail.com
SMTP_PASS=your_gmail_app_password
ALERT_EMAIL=recipient@example.com

### Run the Agent
```bash
python3 main.py
```
--- 

### 📧 Sample Email Output
🕒 2025-07-06 12:18:57.473065  
📦 Container: cpu_hog_app  
📈 CPU Usage: 1033.94%  
🧠 LLM Analysis:  
The container appears to be stuck in a CPU-intensive loop inside app.py.  

🔁 Action Taken:  
ℹ️ Restart not needed — LLM didn’t suggest it.


---
👨‍💻 Author
Vishnu — DevOps Engineer & AI Enthusiast
📧 Contact: 07vishnuatwork@gmail.com
---
