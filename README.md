# ERROR LOG MONITORING PROBLEM SOLUTION
Name: Souhardya Das\
Roll: 002010701134\
Dept: ETCE\
Jadavpur University

# My Approach
The data structure used is a dictionary with a tuple as key and float as value:\
Key : (timestamp, logtype)\
Value: Severity
## Description of main source code.
### A. Parse_Entry
This function takes a string, 'entry', as an argument - which signifies the log entries.\
Step 1:\
Checks the command type: {1,2,3,4}\
Step 2: \
If command = 1, the timestamps (int), log_type, severity (float) are returned\
If command = 2, the log_type, severity (float) is returned\
If command = 3, the timestamps (int) and action ( BEFORE or AFTER) are returned\
If command = 4, the timestamps (int), action ( BEFORE or AFTER) and log_type are returned

### B. Sol
This function takes a string, 'entry', and the main dictionary, 'entry_dict'.\
Step 1:\
Checks the command type: {1,2,3,4}\
Step 2: \
If command = 1, the timestamps (int), log_type, severity (float) are obtained from Parse_entry. Next, the entry_dict is updated with the new log.\
If command = 2, the log_type, severity (float) is obtained. Next, the min, max and average severity values of the errors of the given log_type in the current instance of entry_dict are computed and returned. \
If command = 3, the timestamps (int) and action ( BEFORE or AFTER) are obtained. Next, the min, max and average severity values of the errors of the logs before/after the given timestamp in the current instance of entry_dict are computed and returned.\
If command = 4, the timestamps (int), action ( BEFORE or AFTER) and log_type are obtained. Next, the min, max and average severity values of the errors of the logs before/after the given timestamp and of the given log_type in the current instance of entry_dict are computed and returned.


