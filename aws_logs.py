import json
import random
from datetime import datetime, timedelta

def random_time():
    now = datetime.utcnow()
    random_minutes = random.randint(1, 500)
    return (now - timedelta(minutes=random_minutes)).isoformat() + "Z"

def random_ip():
    return f"192.168.1.{random.randint(1, 254)}"

def read_aws_logs(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    events = []
    for record in data['Records']:
        events.append({
            "cloud": "AWS",
            "time": random_time(),
            "event": record['eventName'],
            "user": record['userIdentity'].get('userName', 'Unknown'),
            "ip": random_ip()
        })

    return events
