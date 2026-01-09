import json

def read_aws_logs(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    events = []
    for record in data['Records']:
        events.append({
            "cloud": "AWS",
            "time": record['eventTime'],
            "event": record['eventName'],
            "user": record['userIdentity'].get('userName', 'Unknown'),
            "ip": record['sourceIPAddress']
        })

    return events
