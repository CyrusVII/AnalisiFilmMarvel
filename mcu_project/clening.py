import pandas as pd

# === 1. Caricamento del file CSV ===
file_path = "mcu_project/mcu-movies-updated.csv"  # Sostituisci con il tuo path locale
df = pd.read_csv(file_path, sep=',')

# === 2. Pulizia dei dati ===

# Rimuove spazi dai nomi delle colonne
df.columns = df.columns.str.strip()

# Rimuove eventuali righe completamente vuote
df.dropna(how='all', inplace=True)

# Riempie i valori nulli con valori ragionevoli
df['running_time'] = df['running_time'].fillna(df['running_time'].mean())
df['budget'] = df['budget'].fillna(df['budget'].mean())
df['box_office'] = df['box_office'].fillna("0")
df['superheroes'] = df['superheroes'].fillna("Unknown")

# Converte le colonne in formati corretti
df['running_time'] = pd.to_numeric(df['running_time'], errors='coerce')
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['box_office'] = pd.to_numeric(df['box_office'], errors='coerce')

# Ordina il DataFrame per ordine di uscita
df = df.sort_values(by='release_order')

# === 3. Il DataFrame pulito è pronto! ===
print(df.head())  # Mostra le prime righe

