import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

def plot_roi(df):
    """Grafico a barre del ROI per ogni film MCU."""
    if 'roi' not in df.columns:
        df = df.copy()
        df['roi'] = (df['box_office'] - df['budget']) / df['budget']

    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(16, 8))

    bars = ax.bar(df['movie'], df['roi'], color='#1f77b4', edgecolor='black')
    ax.set_title("Return on Investment (ROI) - Marvel Cinematic Universe", fontsize=18, weight='bold')
    ax.set_xlabel("Film", fontsize=12)
    ax.set_ylabel("ROI", fontsize=12)
    ax.set_xticks(range(len(df)))
    ax.set_xticklabels(df['movie'], rotation=75, ha='right', fontsize=9)
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ax.set_ylim(0, df['roi'].max() + 1)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    plt.show()

def plot_box_office_trend(df):
    """Grafico a linea dell'andamento degli incassi nel tempo."""
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce', dayfirst=True)

    df_plot = df[['movie', 'release_date', 'box_office']].dropna().sort_values('release_date')

    plt.figure(figsize=(12, 6))
    plt.plot(df_plot['release_date'], df_plot['box_office'], marker='o', linestyle='-', color='darkgreen')
    plt.title('Andamento degli incassi nel tempo - MCU')
    plt.xlabel('Data di uscita')
    plt.ylabel('Box Office (milioni di $)')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
