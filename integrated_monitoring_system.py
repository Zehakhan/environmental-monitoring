import time
from sensor_simulation import simulate_sensor_data
from data_processing import process_data
from data_storage import store_data
from data_visualization import visualize_data

def integrated_system():
    for data in simulate_sensor_data():
        processed_data = process_data(data)
        store_data([processed_data])
        
        # Check for alerts (example: temperature threshold)
        if processed_data['temperature'] > 28.0:
            print(f"Alert! High temperature: {processed_data['temperature']}")
        time.sleep(1)
        
        # Visualize data periodically (e.g., every 10 iterations)
        if int(time.time()) % 10 == 0:
            visualize_data()

if __name__ == "__main__":
    integrated_system()
