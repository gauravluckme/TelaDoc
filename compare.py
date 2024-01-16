import json
from datetime import datetime
import re

# Define a regular expression pattern to extract the version
pattern = r'([vV]\d+\.\d+\.\d+)'

# Path to the input JSON file
json_file_path = "input.json"
with open(json_file_path) as file:
    input_json = json.loads(file.read())

# Path to the input2 JSON file
json_file_path2 = "input2.json"
with open(json_file_path) as file:
    input_json2 = json.loads(file.read())

def version_to_tuple(version_str):
    return tuple(map(int, version_str[1:].split('.')))
# Compare timestamps
for obj1, obj2 in zip(input_json["apps"], input_json2["apps"]):
    version = re.search(pattern, obj1["container"]["docker"]["image"])

    version2 = re.search(pattern, obj2["container"]["docker"]["image"])
    
    if version:
            ver = version.group(1)
            # Parse version strings
            version1 = version_to_tuple(ver)
        
    if version2:
        ver2 = version2.group(1)
        # Parse version strings
        version2 = version_to_tuple(ver2)
    
    if version1 < version2:
        print(f"Version1 {ver} is older than Version2 {ver2}") 
    elif version1 > version2:
        print(f"Version1 {ver} is newer than Version2 {ver2}")
    else:
        print(f"Version1 {ver} is the same as Version2 {ver2}")