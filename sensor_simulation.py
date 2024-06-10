import random
import time

def generate_sensor_data():
    while True:
        temperature = round(random.uniform(20.0, 30.0), 2)
        print(f"Temperature: {temperature}°C")
        time.sleep(1)

generate_sensor_data()
