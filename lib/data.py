import pandas as pd
import numpy as np

def load_df(path_to_yelp_data:str, path_to_race_by_zip="data/race_by_postalcode.csv") -> pd.DataFrame:

    # Einlesen von yelp buisness.json und den "Rasse"-Daten vom stat-atlas
    df = pd.read_json(path_to_yelp_data, lines=True)
    race_df = pd.read_csv(path_to_race_by_zip, sep=",", encoding="utf-8").iloc[:,1:]
    
    # Ausschluss der kanadischen Zeilen, durch Wahl der numerischen ZIP-Codes
    df = df[df.postal_code.str.isnumeric()]
    df.postal_code = df.postal_code.astype("int64")

    # Merge on ZIP-Code für alle Postal-Codes
    merged = pd.merge(df, race_df, on="postal_code", how="left")
    # NaN setzen für deutsche ZIP-Codes nach Längengrad
    merged.loc[merged.longitude > 0, list(race_df.columns)] = np.nan
    # Fehlende Werte ausschließen, wenn mehr als 3 Rassen-Werte fehlen und falls irgendwo der postal_code NaN ist.
    clean_df = merged.dropna(axis=0, thresh=3, subset=list(race_df.columns))
    clean_df = clean_df.dropna(axis=0, subset=["postal_code"])

    return clean_df