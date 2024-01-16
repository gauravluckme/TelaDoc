import os
import json
from collections import defaultdict

# Dictionary to store port information
port_info = defaultdict(list)

# Path to the input JSON file
json_file_path = "input.json"
with open(json_file_path) as file:
    input_json = json.loads(file.read())

# Iterate through applications
for app in input_json['apps']:
    app_id = app['id']
    
    # Iterate through port mappings
    for port_mapping in input_json['apps']:
        container_port = port_mapping["container"]["portMappings"]['containerPort']
        
        # Store application ID for the corresponding port
        port_info[container_port].append(app_id)

# Find applications that share the same ports
duplicate_ports = {port: app_ids for port, app_ids in port_info.items() if len(app_ids) > 1}

# Print the report
if duplicate_ports:
    print("Applications with the same ports:")
    for port, app_ids in duplicate_ports.items():
        print(f"Port {port}: {', '.join(app_ids)}")
else:
    print("No applications share the same ports.")