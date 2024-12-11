from concurrent.futures import ThreadPoolExecutor
import time

def process_chunk(chunk):
    total_requests = 0
    errors = []
    for line in chunk:
        total_requests += 1
        if "Error" in line:
            errors.append(line.strip())
    return total_requests, errors

def split_file(file_path, chunk_size):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

def main():
    file_path = "logs.txt"
    chunk_size = 100
    num_workers = 4

    print("Splitting file into chunks...")
    chunks = split_file(file_path, chunk_size)
    print(f"Total chunks created: {len(chunks)}")

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(process_chunk, chunks))

    total_requests = sum(result[0] for result in results)
    errors = [error for result in results for error in result[1]]

    end_time = time.time()

    print("\n=== Results ===")
    print(f"Total Requests: {total_requests}")
    print(f"Errors: {errors}")
    print(f"Processing Time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
