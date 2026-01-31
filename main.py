import json
import time
import random
from aws_logs import read_aws_logs
from azure_logs import read_azure_logs

AWS_LOG_FILE = 'aws_sample_logs.json'
AZURE_LOG_FILE = 'azure_sample_logs.json'

while True:
    aws_events = read_aws_logs(AWS_LOG_FILE)
    azure_events = read_azure_logs(AZURE_LOG_FILE)

    aws_count = random.randint(1, len(aws_events))
    azure_count = random.randint(1, len(azure_events))

    unified_logs = (
        random.sample(aws_events, aws_count) +
        random.sample(azure_events, azure_count)
    )

    with open('unified_logs.json', 'w', encoding='utf-8') as file:
        json.dump(unified_logs, file, indent=4)

    print("🔄 Logs updated!")
    print(f"🧾 Total Events: {len(unified_logs)}")
    print("⏳ Waiting 5 seconds...\n")

    time.sleep(5)
