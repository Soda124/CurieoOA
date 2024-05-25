## This file describes the working of the test case generator function
1. The random module is imported to facilitate the generation of random values for log entries.\
2. Parameters: num_entries -> The number of log entries to generate.
3. An array of different log types is created. For example: [Error, Warning, Info, Debug, Critical] etc.
4. The timestamp starts at 1 and is incremented as new log entries are generated. Thus they will follow increasing order
5. The first loop generates 30 initial log entries with severities in range [1e-6,1e6] and of random log_types.
6. For the remaining log entries, one of four types of entries is randomly selected
7. If command_type = 3 or 4, the timstamp in the log entry is adjusted by subtracting 30./ This adjusted timestamp is used to create a meaningful filter based on a prior timestamp.
8. All the log_entries are written in a .txt file
