import json
import random
from datetime import datetime, timedelta

def random_time():
    now = datetime.utcnow()
    random_minutes = random.randint(1, 500)
    return (now - timedelta(minutes=random_minutes)).isoformat() + "Z"

def random_ip():
    return f"10.0.0.{random.randint(1, 254)}"

def read_azure_logs(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    events = []
    for record in data['value']:
        events.append({
            "cloud": "Azure",
            "time": random_time(),
            "event": record['operationName'],
            "user": record['caller'],
            "ip": random_ip()
        })

    return events
