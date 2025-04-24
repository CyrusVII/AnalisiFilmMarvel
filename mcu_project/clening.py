import pandas as pd
import sqlite3

def take_data():
  
  # Caricamento del CSV
  file_path = "mcu_project/mcu-movies-updated.csv"
  df = pd.read_csv(file_path)

  # Visualizzazione delle prime righe
  print("Prime righe del DataFrame:")
  print(df.head())

  # Informazioni generali
  print("\nInformazioni del DataFrame:")
  print(df.info())

  # Colonna: movie
  # -> stringa, lasciamo così, ma possiamo rimuovere spazi extra se ci sono
  df['movie'] = df['movie'].str.strip()

  # Colonna: release_date
  # -> convertire in datetime
  df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

  # Colonne: release_order, chronological_order, phase
  # -> float64, possono essere convertiti in int se non ci sono decimali
  df['release_order'] = df['release_order'].astype('int')
  df['chronological_order'] = df['chronological_order'].astype('int')
  df['phase'] = df['phase'].astype('int')

  # Colonna: running_time
  df['running_time'] = df['running_time'].astype('int')

  # Colonna: budget
  # -> float, ok,  convertire a milioni 
  df['budget'] = df['budget'] 

  # Colonna: box_office
  # dobbiamo pulire e convertire in numero
  df['box_office'] = df['box_office'].replace('[\$,]', '', regex=True).replace(',', '', regex=True)
  df['box_office'] = pd.to_numeric(df['box_office'], errors='coerce')  

  # Colonne: rt_critic_score e rt_audience_score
  # -> già float, ma potresti normalizzare su 0-1 (opzionale)
  df['rt_critic_score'] = df['rt_critic_score'] / 100
  df['rt_audience_score'] = df['rt_audience_score'] / 100

  # Colonna: superheroes
  # -> se contiene liste o stringhe multiple, potremmo dividerla
  df['superheroes_list'] = df['superheroes'].str.split(',\s*')

  # Mostra le colonne disponibili 
  print("\nColonne disponibili:")
  print(df.columns)
  
  return df






