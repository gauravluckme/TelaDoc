import os
import json
from datetime import datetime

# Accept user input as a string
hours_threshold = input("Enter a hours to check aplication that have changed their config: ")

try:
    # Convert the string to an integer
    hours_threshold = int(hours_threshold)
    
    # Print the result
    print("The entered hours threshold is:", hours_threshold)

    # Path to the input JSON file
    json_file_path = "input.json"
    with open(json_file_path) as file:
        input_json = json.loads(file.read())

        # Get the current time in UTC
        current_time_utc = datetime.utcnow()

        # Format the current time as a string
        current_formatted_time = current_time_utc.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'

        app_data = {}
        app_list = []

        for data in input_json["apps"]:
            last_modified_time = data["versionInfo"]["lastConfigChangeAt"]
            
            # Convert timestamp strings to datetime objects
            last_modified_timetamp = datetime.strptime(last_modified_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            current_formatted_timestamp = datetime.strptime(current_formatted_time, "%Y-%m-%dT%H:%M:%S.%fZ")

            time_difference = current_formatted_timestamp - last_modified_timetamp
            #print(time_difference.total_seconds(), hours_threshold * 3600)
            
            if time_difference.total_seconds() <= hours_threshold * 3600:
                application_name = data["id"].split("/")[2]
                config_change_time = data["versionInfo"]["lastConfigChangeAt"]
                app_data = {"application_name": application_name, "config_change_time": config_change_time}
                app_list.append(app_data)
        
        # Iterate the application list
        for app in app_list:
            app["config_change_time"] = datetime.strptime(app["config_change_time"], "%Y-%m-%dT%H:%M:%S.%fZ")

        # Sort the applications based on config change time
        sorted_applications = sorted(app_list, key=lambda x: x["config_change_time"], reverse=True)

        # Print the sorted applications
        for app in sorted_applications:
            print(f"Application Name: {app['application_name']} | Config Change Time: {app['config_change_time'].strftime('%Y-%m-%dT%H:%M:%S.%fZ')}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")