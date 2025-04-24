# main.py
from utils import load_data, clean_data, calculate_roi
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Percorso al file CSV
csv_path = "C:/Users/stefa/OneDrive/Desktop/AnalisiFilmMarvel/mcu_project/mcu-movies-updated.csv"

# 1. Caricamento dati
df = load_data(csv_path)

# 2. Pulizia dati
df = clean_data(df)

# 3. Calcolo ROI
df = calculate_roi(df)

# 4. Stampa overview
print("\nPrime 5 righe del DataFrame pulito con ROI:")
print(df.head())

# 5. Grafico ROI 
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

# Aggiunta etichette sopra le barre
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # spostamento in pixel
                textcoords="offset points",
                ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()