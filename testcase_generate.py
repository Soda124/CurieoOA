import random

def generate_test_input(num_entries):
    types = ['ERROR', 'WARNING', 'INFO', 'DEBUG', 'CRITICAL', 'ALERT',
             'NOTICE', 'EMERGENCY', 'TRACE', 'FATAL', 'SECURITY', 'AUDIT',
             'INFO', 'PERFORMANCE', 'CONFIG']
    timestamp = 1
    with open('/Users/souhardyadas/Desktop/assignment/input1.txt', 'w') as file:
        for _ in range(30):
            log_type = random.choice(types)
            timestamp += random.randint(1,5)
            severity = round(random.uniform(1e-6,1e6),2)
            file.write(f"1 {timestamp};{log_type};{severity}\n")
        for _ in range(num_entries):
            choice = random.choices([1, 2, 3, 4], weights=[0.4, 0.3, 0.15, 0.15])[0]
            if choice == 1:
                log_type = random.choice(types)
                severity = round(random.uniform(1e-6,1e6),2)
                timestamp += random.randint(1,5)
                file.write(f"1 {timestamp};{log_type};{severity}\n")
            elif choice == 2:
                log_type = random.choice(types)
                file.write(f"2 {log_type}\n")
            elif choice == 3:
                subcommand = random.choice(['BEFORE', 'AFTER'])
                timestamp += random.randint(1,5)
                file.write(f"3 {subcommand} {timestamp-30}\n")
            elif choice == 4:
                subcommand = random.choice(['BEFORE', 'AFTER'])
                log_type = random.choice(types)
                timestamp += random.randint(1,5)
                file.write(f"4 {subcommand} {log_type} {timestamp-30}\n")
if __name__ == "__main__":
    generate_test_input(300)