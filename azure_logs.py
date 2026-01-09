import json

def read_azure_logs(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    events = []
    for record in data['value']:
        events.append({
            "cloud": "Azure",
            "time": record['timeGenerated'],
            "event": record['operationName'],
            "user": record['caller'],
            "ip": record['ipAddress']
        })

    return events
