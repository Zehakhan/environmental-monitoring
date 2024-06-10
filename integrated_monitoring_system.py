import random
import time
import csv
import matplotlib.pyplot as plt

# Sensor Simulation
def generate_sensor_data():
    while True:
        temperature = round(random.uniform(20.0, 30.0), 2)
        process_data(temperature)
        time.sleep(1)

# Data Processing
def process_data(data):
    fahrenheit = data * 1.8 + 32
    store_data(fahrenheit)

# Data Storage
def store_data(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data])
    monitor_data(data)

# Data Visualization
def visualize_data():
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(float(row[0]))
    plt.plot(data)
    plt.show()

# Monitoring System
def monitor_data(data):
    if data > 77:  # Equivalent to 25°C
        print("Alert: High temperature!")

# Run the entire system
generate_sensor_data()
