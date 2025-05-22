### Q23: Create 3 CSV files for each call type: "Received," "Declined," and "Called" with the respective call logs.

"""
Data Loading
Data cleaning
EDA - Exploratory Data Analysis
- Data Analysis
- Data Visualization

Data Preprocessing
- Feature Engineering
- Feature Selection

Model Training
Model Evaluation
Model Prediction
Deploy

"""

import csv

with open("call_logs.csv", "r") as f:
    reader = csv.DictReader(f)
    call_logs = list(reader)

print(call_logs)
print(len(call_logs))

declined_logs = []  # list of dictionary
received_logs = []
called_logs = []

for call in call_logs:
    status = call["Status"]

    if status == "Declined":
        declined_logs.append(call)
    
    elif status == "Received":
        received_logs.append(call)
    
    elif status == "Called":
        called_logs.append(call)

print(len(declined_logs))
print(len(received_logs))
print(len(called_logs))

# header = ["Name", "Call ID", "Duration (Seconds)", "Status"]

def create_csv_file(filename, data):
    header = data[0].keys()
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

create_csv_file("declined_calls.csv", declined_logs)
create_csv_file("received_calls.csv", received_logs)
create_csv_file("called_calls.csv", called_logs)