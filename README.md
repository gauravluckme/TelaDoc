Please find the below file view:

.
├── README.md
├── compare.py
├── input.json
├── input2.json
├── main.py
└── port.py

main.py - It is performing the below operations.
1. Obtain all the aplication that have changed their config on the last X hours.
2. Output mas have the name of each application and the date it was modified in.
3. Last modified application must be shown first.

Usage: 

    Run "python main.py"
    Then, it will ask for user input
        Enter a hours to check aplication that have changed their config: 
    Enter a hours to check aplication that have changed their config.
    The result will be displayed

port.py - It is performing the below operations.
1. Find the applications that have the same ports and make a report.

Usage: 

    Run "python port.py"

compare.py - It is performing the below operations.
1. Find the diferences of versions between two json files and determine which is the most recent version of the component the format for the images is as follows:
    Registry/component:version-date-hour

Usage: 

    Run "python compare.py"

Note: The data in the json is not proper some field are missing so the script may throw error, we can make the script better by adding error handling.