# main.py
from utils import load_data, clean_data, calculate_roi
import matplotlib.pyplot as plt

# Percorso al CSV
csv_path = "mcu_movies_with_protagonist.csv"

# 1. Caricamento dati
df = load_data(csv_path)

# 2. Pulizia dati
df = clean_data(df)

# 3. Calcolo ROI
df = calculate_roi(df)

# 4. Stampa overview
print("\nPrime 5 righe del DataFrame pulito con ROI:")
print(df.head())

# 5. Grafico ROI (esempio)
plt.figure(figsize=(10, 5))
plt.plot(df['release_order'], df['roi'], marker='o')
plt.title("MCU ROI per Film (ordine di uscita)")
plt.xlabel("Release Order")
plt.ylabel("ROI")
plt.grid(True)
plt.xticks(df['release_order'], df['movie'], rotation=90)
plt.tight_layout()
plt.show()
