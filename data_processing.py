def process_data(data):
    # Example processing: Convert to a dictionary
    processed_data = {
        'timestamp': data[0],
        'temperature': data[1],
        'humidity': data[2],
        'air_quality': data[3]
    }
    return processed_data
