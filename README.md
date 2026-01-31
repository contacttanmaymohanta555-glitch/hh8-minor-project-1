☁️ Offline Cloud Log Monitoring System






📌 Project Overview

The Offline Cloud Log Monitoring System is a Python-based project that demonstrates how cloud logs from multiple providers (AWS & Azure) can be collected, normalized, and analyzed centrally.

🔹 Instead of using live cloud APIs, this project uses offline JSON log files for academic and demonstration purposes.
🔹 This makes the project easy to run, error-free, and ideal for college submissions and viva.

🎯 Objectives

📊 Understand cloud log monitoring concepts

🔐 Learn how security events are recorded in cloud platforms

🔄 Normalize logs from different cloud providers

🧠 Demonstrate centralized log analysis without real cloud access

🎓 Build a minor project suitable for academic evaluation

🧠 Problem Statement

Cloud environments generate huge volumes of logs across multiple services and providers.
Monitoring these logs individually is inefficient and error-prone.

❓ How can we unify and analyze logs from different cloud platforms in a centralized way?

✅ Solution: A unified offline cloud log monitoring system.

🛠️ Technology Stack
Component	Technology
Language	🐍 Python 3
Log Format	📄 JSON
Cloud Logs	☁️ AWS CloudTrail (Sample), Azure Monitor (Sample)
IDE	💻 Visual Studio Code
Platform	🖥️ Cross-platform (Windows / Linux / macOS)
📁 Project Folder Structure
cloud-log-monitoring-offline
│
├── aws_sample_logs.json        # Sample AWS CloudTrail logs
├── azure_sample_logs.json      # Sample Azure Monitor logs
├── aws_logs.py                 # AWS log parser
├── azure_logs.py               # Azure log parser
├── main.py                     # Main program
├── unified_logs.json           # Output file (auto-generated)
└── README.md                   # Project documentation

⚙️ How the Project Works
🔹 Step 1: Read Cloud Logs

AWS and Azure logs are stored as JSON files

Each cloud has a separate parser module

🔹 Step 2: Normalize Logs

Logs are converted into a common structure

Fields like:

Cloud Provider

Timestamp

Event Name

User

IP Address

🔹 Step 3: Merge Logs

AWS + Azure logs are combined into a single list

🔹 Step 4: Store Unified Logs

Final output is written to:

unified_logs.json

▶️ How to Run the Project
✅ Prerequisites

Python 3 installed

VS Code (recommended)

🧪 Steps to Execute
python main.py

🎉 Successful Output
Unified Cloud Logs Created Successfully!
Total Events: 4


📄 A new file unified_logs.json will be created.

📄 Sample Output (Unified Logs)
{
  "cloud": "AWS",
  "time": "2025-01-10T10:15:30Z",
  "event": "ConsoleLogin",
  "user": "admin",
  "ip": "192.168.1.10"
}

🔍 Key Features

✅ Offline execution (No AWS/Azure account needed)

✅ Centralized log monitoring concept

✅ Modular and clean Python code

✅ Beginner-friendly

✅ Viva & demo ready

🧪 Why Offline Mode?

🔐 Live cloud APIs require:

Paid accounts

Access keys

Internet dependency

🎓 For academic projects, offline logs:

Avoid authentication issues

Ensure smooth demo

Focus on conceptual learning

🧑‍🏫 Viva Explanation (Important)

“This project demonstrates centralized cloud log monitoring by normalizing AWS CloudTrail and Azure Monitor logs into a unified format. For academic purposes, offline log files are used instead of real-time cloud APIs.”

🚀 Future Enhancements

🔔 Suspicious activity detection

📊 Log analytics & filtering

🌐 Flask-based web dashboard

☁️ Real AWS & Azure API integration

🧠 SIEM-style alerting system

👨‍💻 Author

Name: Tanmay Mohanta

Course: B.Tech

Domain: Cybersecurity

Year: 2022–2026
