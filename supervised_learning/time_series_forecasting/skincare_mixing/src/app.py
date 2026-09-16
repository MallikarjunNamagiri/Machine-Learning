import os

import pandas as pd

def load_data(data):
    """
    Load data from a CSV file into a pandas DataFrame.
    """
    
    # Load the CSV file into a DataFrame
    df = pd.read_excel(data)
    return df


def greet(name, greeting="Hi"):
    return f"{greeting}, My Name is {name}..!"   

