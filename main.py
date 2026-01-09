import json
from aws_logs import read_aws_logs
from azure_logs import read_azure_logs

AWS_LOG_FILE = 'aws_sample_logs.json'
AZURE_LOG_FILE = 'azure_sample_logs.json'

aws_events = read_aws_logs(AWS_LOG_FILE)
azure_events = read_azure_logs(AZURE_LOG_FILE)

unified_logs = aws_events + azure_events

with open('unified_logs.json', 'w') as file:
    json.dump(unified_logs, file, indent=4)

print("Unified Cloud Logs Created Successfully!")
print(f"Total Events: {len(unified_logs)}")
import json
from aws_logs import read_aws_logs
from azure_logs import read_azure_logs

AWS_LOG_FILE = 'aws_sample_logs.json'
AZURE_LOG_FILE = 'azure_sample_logs.json'

aws_events = read_aws_logs(AWS_LOG_FILE)
azure_events = read_azure_logs(AZURE_LOG_FILE)

unified_logs = aws_events + azure_events

with open('unified_logs.json', 'w') as file:
    json.dump(unified_logs, file, indent=4)

print("Unified Cloud Logs Created Successfully!")
print(f"Total Events: {len(unified_logs)}")