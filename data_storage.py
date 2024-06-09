import pandas as pd

def store_data(data):
    df = pd.DataFrame(data)
    df.to_csv('environmental_data.csv', mode='a', header=False, index=False)
