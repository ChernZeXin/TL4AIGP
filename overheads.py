from pathlib import Path
import csv

def read_and_process_file():
    # Read the CSV file and process the records
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        records = [[row[0], float(row[1])] for row in reader]  # Use list comprehension to read records
    return records

def find_highest_overhead():
    # Find the highest overhead
    highest_overhead = 0.0
    highest_category = ""
    for category, overhead in overheads:
        if overhead > highest_overhead:
            highest_overhead = overhead
            highest_category = category
    return highest_category, highest_overhead

def output_overhead(cat, highest):
    # Format the output string
    output = f'[HIGHEST OVERHEAD] {cat.upper()}: {highest}%\n'
    return output

def overhead_function():
    # Define the file path
    file_path = Path.cwd() / "csv_reports" / "Overheads.csv"

    # Read and process the CSV file
    overheads = read_and_process_file(file_path)

    # Identify the highest overhead
    cat, highest = find_highest_overhead(overheads)

    # Generate the output string
    output = output_overhead(cat, highest)

    # Write the output to the Summary_report.txt file
    with open('Summary_report.txt', 'w') as f:
        f.write(output)
