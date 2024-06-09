import pandas as pd

def store_data(data):
    df = pd.DataFrame(data)
    df.to_csv('environmental_data.csv', index=False)
