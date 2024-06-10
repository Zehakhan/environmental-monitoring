def process_data(data):
    return data * 1.8 + 32  # Convert Celsius to Fahrenheit

# Example test
celsius = 25.0
fahrenheit = process_data(celsius)
print(f"Celsius: {celsius}, Fahrenheit: {fahrenheit}")
