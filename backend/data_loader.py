# backend/data_loader.py

import pandas as pd

def get_data():
    df = pd.read_csv(
        "data/transport_saas_6months_30000_rows.csv"
    )
    return df