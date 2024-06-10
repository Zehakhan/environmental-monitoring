import csv

def store_data(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data])

# Example test
store_data(77.0)

# Verify storage
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
