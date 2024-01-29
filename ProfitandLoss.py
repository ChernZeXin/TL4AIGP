from pathlib import Path
import csv

# Read and process "Profit & Loss.csv" to calculate net profit differences
def read_and_process_file():
    # Define the path to the CSV file
    file_path = Path.cwd() / "csv_reports" / "Profit & Loss.csv"
    # Open the CSV file and read its contents
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        # Extract the day and net profit for each record
        records = [[row[0]] + [int(row[4])] for row in reader]

    # Calculate the difference in net profit from the previous day
    for i in range(1, len(records)):
        profit_diff = records[i][1] - records[i-1][1]
        records[i].append(profit_diff)
    # The first record has no previous day for comparison
    records[0].append(0)
    return records

# Identify the trend in net profits and generate the appropriate output
def identify_trend_and_generate_output(records):
    # Check if the net profits are always increasing
    increasing = all(record[2] >= 0 for record in records[1:])
    # Check if the net profits are always decreasing
    decreasing = all(record[2] <= 0 for record in records[1:])

    # Generate output based on the identified trend
    if increasing:
        day, highest_increase = max(records[1:], key=lambda x: x[2])
        output = f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n[HIGHEST NET PROFIT SURPLUS] DAY: {day}, AMOUNT: USD{highest_increase}\n'
    elif decreasing:
        day, highest_decrease = min(records[1:], key=lambda x: x[2])
        output = f'[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY\n[HIGHEST NET PROFIT DEFICIT] DAY {day}, AMOUNT: USD{-highest_decrease}\n'
    else:
        deficits = [(record[0], record[2]) for record in records if record[2] < 0]
        top3_deficits = sorted(deficits, key=lambda x: x[1])[:3]
        output = ''.join([f'[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{-amount}\n' for day, amount in top3_deficits])

    return output

# Main function to process the "Profit & Loss.csv" file and append the result to "Summary_report.txt"
def profit_loss_function():
    records = read_and_process_file()
    output = identify_trend_and_generate_output(records)

    # Append the output to "Summary_report.txt"
    with open('Summary_report.txt', 'a') as f:
        f.write(output)

# Execute the main function

