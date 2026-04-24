import pandas as pd

def load_logs():
    df = pd.read_csv("data/splunk_logs.csv")
    return df

def preprocess_logs(df):
    # Keep only useful columns if they exist
    useful_columns = [col for col in ["Time", "Event"] if col in df.columns]

    if useful_columns:
        df = df[useful_columns]

    return df.head(100).to_string(index=False)
