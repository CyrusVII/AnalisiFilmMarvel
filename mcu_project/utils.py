# utils.py
import pandas as pd
import numpy as np  # opzionale

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    df = df.copy()
    df['release_date'] = pd.to_datetime(df['release_date'], format="%d-%b-%y", errors='coerce')

    df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
    df['box_office'] = pd.to_numeric(df['box_office'], errors='coerce')
    return df

def calculate_roi(df):
    df = df.copy()
    df['roi'] = (df['box_office'] - df['budget']) / df['budget']
    return df
