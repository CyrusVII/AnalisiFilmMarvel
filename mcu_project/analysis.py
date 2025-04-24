import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analizza_guadagni_mcu(df):
    # Calcolo del profitto
    df['profit'] = df['box_office'] - df['budget']

    profit_medio = float(np.mean(df['profit']))
    profit_massimo = float(np.max(df['profit']))
    profit_minimo = float(np.min(df['profit']))

    # Film con profitto massimo e minimo
    film_max_profit = df.loc[df['profit'].idxmax(), 'movie']
    film_min_profit = df.loc[df['profit'].idxmin(), 'movie']

    # Dizionario dei risultati
    risultati = {
        "profit medio": round(profit_medio, 1),
        "profit massimo": round(profit_massimo, 1),
        "film con profit massimo": film_max_profit,
        "profit minimo": round(profit_minimo, 1),
        "film con profit minimo": film_min_profit
    }

    # Converte in DataFrame e salva in CSV
    risultati_df = pd.DataFrame([risultati])
    risultati_df.to_csv("risultati_guadagni_mcu.csv", index=False)

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
