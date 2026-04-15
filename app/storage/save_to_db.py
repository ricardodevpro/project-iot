from app.config.database import get_engine

def save_data(df):
    engine = get_engine()
    df.to_sql("temperature_readings", engine, if_exists="replace", index=False)
    print("Dados salvos no banco!")