# 🛡️ Cloud Log Monitor (Offline)

A professional cybersecurity tool designed to ingest, normalize, and unify security logs from multiple cloud providers (**AWS** and **Azure**). This project simulates a simplified **SIEM (Security Information and Event Management)** data pipeline, transforming provider-specific JSON logs into a standardized format for centralized security monitoring.

---

## 📌 Project Overview
Monitoring disparate cloud environments is a significant challenge in modern security operations. This project provides an automated pipeline that:
- **Ingests** raw AWS CloudTrail-style logs and Azure Activity logs.
- **Normalizes** varying data schemas into a single Unified Log format.
- **Simulates** real-time log updates to provide a continuous stream of security events for analysis.

## ✨ Features
- ✅ **Multi-Cloud Support**: Native handling for AWS and Azure log structures.
- ✅ **Data Normalization**: Standardizes fields like `cloud`, `event`, `user`, `ip`, and `time` across platforms.
- ✅ **Real-time Simulation**: Periodically updates the unified log file with random event samples every 5 seconds.
- ✅ **Automated Metadata Spoofing**: Generates realistic timestamps and IP addresses for simulation purposes.
- ✅ **Extensible Design**: Easy to add support for GCP or custom on-premise logs.

---

## 🧱 Project Architecture
The system utilizes a modular Python architecture to handle different cloud data schemas:

1. **Provider Modules (`aws_logs.py`, `azure_logs.py`)**: Individual parsers that read raw JSON and map them to the unified schema.
2. **Core Engine (`main.py`)**: The central orchestrator that manages the loop, samples events, and writes the `unified_logs.json`.
3. **Data Layer**: Raw sample logs provided in JSON format to simulate cloud provider outputs.



---

## 🛠️ Technologies Used
- **Python 3.x**: Core logic and data processing.
- **JSON**: Data storage and interchange format.
- **Standard Libraries**: `datetime`, `random`, and `time` for simulation logic.

---

## 📂 Project Structure
```text
EndpointSecurityMonitor/
│
├── main.py               # Main simulation and aggregation engine
├── aws_logs.py           # AWS specific parsing logic
├── azure_logs.py         # Azure specific parsing logic
├── aws_sample_logs.json  # Mock AWS CloudTrail data
├── azure_sample_logs.json # Mock Azure Activity data
└── unified_logs.json     # The final normalized output file
