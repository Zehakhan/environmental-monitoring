import matplotlib.pyplot as plt
import csv

def visualize_data():
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(float(row[0]))
    plt.plot(data)
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Over Time')
    plt.show()

# Example test
visualize_data()

