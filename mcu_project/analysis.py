import pandas as pd
import numpy as np

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

def film_supereroe_piu_presente(df):
    # Espandi i supereroi in righe singole
    data_eroi = df[['movie', 'superheroes']].copy()
    data_eroi['superhero'] = data_eroi['superheroes'].str.split(', ')
    data_eroi = data_eroi.explode('superhero')

    # Conta le presenze e trova il supereroe più presente
    supereroe_top = data_eroi['superhero'].value_counts().idxmax()

    # Filtra i film dove appare quel supereroe
    film_top = data_eroi[data_eroi['superhero'] == supereroe_top]['movie'].unique()

    # Stampa risultati
    print(f"🦸 Supereroe più presente: {supereroe_top}")
    print("📽️ Film in cui compare:")
    for film in sorted(film_top):
        print(f"- {film}")

    return supereroe_top, film_top

