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

def visualizza_andamento_incassi(df):
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce', dayfirst=True)

    # Selezione e ordinamento dei dati
    df_plot = df[['movie', 'release_date', 'box_office']].dropna().sort_values('release_date')

    # Creazione del grafico
    plt.figure(figsize=(12, 6))
    plt.plot(df_plot['release_date'], df_plot['box_office'], marker='o')

    # Aggiunta delle etichette
    plt.title('Andamento degli incassi nel tempo - MCU')
    plt.xlabel('Data di uscita')
    plt.ylabel('Box Office (milioni di $)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    # Visualizzazione
    plt.show()