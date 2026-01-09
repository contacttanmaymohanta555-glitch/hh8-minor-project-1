# hh8-minor-project-1
Multi-Cloud Real-Time Audit & Log Monitor(Offline)

A Python-based monitoring solution that consolidates logs from AWS CloudTrail and Azure Monitor into a unified view. The system identifies "Impossible Travel" scenarios by alerting when a user logs in from two different countries within a single hour across different cloud providers.

📁 Project Structure
main.py: The core engine that runs real-time threads to aggregate logs and process alerts.

aws_logs.py: Contains logic to interface with AWS CloudWatch/S3 for CloudTrail events.

azure_logs.py: Contains logic to stream logs from Azure Event Hub.

unified_logs.json: The consolidated output file where all cross-cloud events are stored in a standardized format.

aws_sample_logs.json / azure_sample_logs.json: Sample data files for testing the logic without live cloud connections.
