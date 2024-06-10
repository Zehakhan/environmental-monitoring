def monitor_data(data):
    if data > 77:  # Equivalent to 25°C
        print("Alert: High temperature!")

# Example test
data = [23.0, 24.0, 26.5, 27.0]
for value in data:
    monitor_data(value)
