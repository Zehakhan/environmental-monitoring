import time
from sensor_simulation import simulate_sensor_data
from data_processing import process_data
from data_storage import store_data
from data_visualization import visualize_data

def integrated_system(max_iterations=100, visualize_every=10):
    iteration_count = 0
    try:
        for data in simulate_sensor_data():
            processed_data = process_data(data)
            store_data([processed_data])
            
            # Check for alerts (example: temperature threshold)
            if processed_data['temperature'] > 28.0:
                print(f"Alert! High temperature: {processed_data['temperature']}")
            time.sleep(1)
            
            iteration_count += 1
            if iteration_count % visualize_every == 0:
                visualize_data()
            
            if iteration_count >= max_iterations:
                break
    except KeyboardInterrupt:
        print("Shutting down gracefully...")

if __name__ == "__main__":
    integrated_system()
