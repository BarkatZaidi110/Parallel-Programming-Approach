import time

def process_log(file_path):
    total_requests = 0
    errors = []
    with open(file_path, 'r') as f:
        for line in f:
            total_requests += 1
            if "Error" in line:
                errors.append(line.strip())
    return total_requests, errors

start_time = time.time()
total_requests, errors = process_log("logs.txt")
print(f"Total Requests: {total_requests}")
print(f"Errors: {errors}")
print(f"Linear Processing Time: {time.time() - start_time} seconds")
