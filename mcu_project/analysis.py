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


def analizza_scores(df):

    # Differenza tra punteggio pubblico e critici
    df['differenza'] = df['rt_audience_score'] - df['rt_critic_score']

    # Film dove il pubblico è stato molto più positivo dei critici
    film_pubblico_piu_positivo = df.loc[df['differenza'].idxmax(), ['movie', 'rt_critic_score', 'rt_audience_score']]

    # Film dove i critici sono stati molto più positivi del pubblico
    film_critici_piu_positivi = df.loc[df['differenza'].idxmin(), ['movie', 'rt_critic_score', 'rt_audience_score']]

    return {
        "film più positivo secondo il pubblico": film_pubblico_piu_positivo.to_dict(),
        "film critici più positivi": film_critici_piu_positivi.to_dict()
    }

def conta_supereroi(df):
    # Divide i nomi dei supereroi separati da virgola e li espande in righe singole
    data_eroi = df['superheroes'].str.split(', ').explode()

    # Conta quante volte ogni supereroe appare
    conteggio = data_eroi.value_counts().reset_index()
    conteggio.columns = ['superhero', 'num_film']
    # Supereroe più presente
    supereroe_max = conteggio.iloc[0]
    print(f"🦸 Supereroe più presente: {supereroe_max['superhero']} ({supereroe_max['num_film']} film)")


    return conteggio
