from app.ingestion.load_csv import load_data
from app.processing.transform import transform_data
from app.storage.save_to_db import save_data

def run():
    path = "data/temperature_readings.csv"

    print("Lendo dados...")
    df = load_data(path)

    print("Transformando dados...")
    df = transform_data(df)

    print("Salvando no banco...")
    save_data(df)

    print("Pipeline finalizado!")

if __name__ == "__main__":
    run()