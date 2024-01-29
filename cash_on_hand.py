from pathlib import Path
import csv

# Function to read "Cash-On-Hand.csv" and parse contents into a list
def read_file():
    fp = Path.cwd() / "csv_reports" / "Cash-On-Hand.csv"
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        coh = [[row[0], int(row[1])] for row in reader]  # Day and cash on hand
    return coh

# Function to calculate daily difference in cash on hand
def calculate_difference(records):
    for i in range(len(records)):
        if i == 0:
            records[i].append(0)  # First record has no previous day to compare
        else:
            difference = records[i][1] - records[i-1][1]
            records[i].append(difference)
    return records

# Function to determine the overall trend in cash on hand
def determine_trend(records):
    differences = [record[2] for record in records]
    if all(d >= 0 for d in differences[1:]):
        return 'increasing'
    elif all(d <= 0 for d in differences[1:]):
        return 'decreasing'
    else:
        return 'fluctuating'

# Function to generate output based on the trend
def generate_output(trend, records):
    if trend == 'increasing':
        day, _, highest = max(records[1:], key=lambda x: x[2])
        return f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n[HIGHEST CASH SURPLUS] DAY: {day}, AMOUNT: USD{highest}\n'
    elif trend == 'decreasing':
        day, _, lowest = min(records[1:], key=lambda x: x[2])
        return f'[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN PREVIOUS DAY\n[HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: USD{-lowest}\n'
    else:  # Fluctuating
        deficits = sorted([(record[0], record[2]) for record in records if record[2] < 0], key=lambda x: x[1])
        output = ''.join([f'[CASH DEFICIT] DAY: {day}, AMOUNT: USD{-amount}\n' for day, amount in deficits[:3]])
        return output

# Main function to process "Cash-On-Hand.csv" and append result to "Summary_report.txt"
def coh_function():
    records = calculate_difference(read_file())
    trend = determine_trend(records)
    output = generate_output(trend, records)
    with open('Summary_report.txt', 'a') as f:
        f.write(output)

# Execute the main function

