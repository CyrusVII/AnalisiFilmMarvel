import pandas as pd
import numpy as np

def analizza_guadagni_mcu(df, salva_csv=True):
    """
    Calcola e restituisce il profitto medio, massimo e minimo dei film MCU.
    Salva i risultati su CSV se salva_csv=True.
    """
    df['profit'] = df['box_office'] - df['budget']

    risultati = {
        "profit medio": round(df['profit'].mean(), 1),
        "profit massimo": round(df['profit'].max(), 1),
        "film con profit massimo": df.loc[df['profit'].idxmax(), 'movie'],
        "profit minimo": round(df['profit'].min(), 1),
        "film con profit minimo": df.loc[df['profit'].idxmin(), 'movie']
    }

    if salva_csv:
        pd.DataFrame([risultati]).to_csv("risultati_guadagni_mcu.csv", index=False)

    return risultati
