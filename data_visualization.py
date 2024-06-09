import pandas as pd
import matplotlib.pyplot as plt

def visualize_data():
    # Example data
    data = pd.read_csv('environmental_data.csv', names=['timestamp', 'temperature', 'humidity', 'air_quality'])
    
    # Plot data
    plt.figure(figsize=(10, 6))
    plt.plot(data['timestamp'], data['temperature'], label='Temperature')
    plt.plot(data['timestamp'], data['humidity'], label='Humidity')
    plt.plot(data['timestamp'], data['air_quality'], label='Air Quality')
    
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.title('Environmental Data')
    plt.legend()
    plt.show()
