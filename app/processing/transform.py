import pandas as pd

def transform_data(df):
    # padronizar nomes
    df.columns = [col.lower() for col in df.columns]

    # renomear colunas problemáticas
    df.rename(columns={
        "room_id/id": "device_id",
        "noted_date": "timestamp",
        "temp": "temperature",
        "out/in": "location"
    }, inplace=True)

    # converter timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="%d-%m-%Y %H:%M")

    return df