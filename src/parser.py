import pandas as pd


def load_transactions(filepath):
    try:
        df = pd.read_csv(filepath)

        df.columns = [col.strip().capitalize() for col in df.columns]

        df['Date'] = pd.to_datetime(df['Date'])
        df['Amount'] - df['Amount'].astype(float)

        return df

    except Exception as e:
        print(f"Error loading transactions: {e}")
        return None
