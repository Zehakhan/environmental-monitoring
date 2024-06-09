import random
import time

def simulate_sensor_data():
    while True:
        data = [
            time.time(),
            random.uniform(20.0, 30.0),  # temperature
            random.uniform(30.0, 60.0),  # humidity
            random.uniform(0.0, 100.0)   # air quality
        ]
        yield data
        time.sleep(1)  # simulate data every second
