
# 🎬 MCU Movies Analysis

Un progetto Python per l'analisi dei film del **Marvel Cinematic Universe (MCU)**. Utilizza i dati aggiornati dei film per esplorare metriche finanziarie, punteggi della critica e del pubblico, presenza dei supereroi e altro ancora, con visualizzazioni interattive.

---

## 📁 Struttura del Progetto

```
mcu_project/
│
├── mcu-movies-updated.csv        # Dataset dei film MCU
├── main.py                       # Menu principale CLI per analisi e visualizzazioni
├── clening.py                    # Funzione per pulizia e caricamento dei dati
├── analysis.py                   # Funzioni di analisi (profitto, scores, supereroi)
├── plots.py                      # Funzioni per visualizzazioni (ROI, box office, correlazioni)
├── risultati_guadagni_mcu.csv   # Output CSV con analisi dei guadagni
└── README.md                     # Documentazione del progetto
```

---

## 🚀 Come Iniziare

### 1. **Requisiti**

Assicurati di avere installato Python 3.7+ e i seguenti pacchetti:

```bash
pip install pandas matplotlib numpy
```

### 2. **Esecuzione**

Esegui il file `main.py`:

```bash
python main.py
```

Segui il menu interattivo per esplorare i dati del MCU.

---

## 📊 Funzionalità Disponibili

### Menu Analitico:
1. **ROI per film**  
   Mostra il *Return on Investment* di ogni film.

2. **Andamento incassi nel tempo**  
   Line chart che rappresenta l'evoluzione del box office.

3. **Analisi dei guadagni (media, max, min)**  
   Calcola e salva in CSV statistiche su profitti.

4. **Confronto Critici vs Pubblico**  
   Trova i film con più discrepanze tra critica e pubblico.

5. **Conteggio dei supereroi**  
   Quante volte appare ciascun supereroe nei film.

6. **Film del supereroe più presente**  
   Mostra i film in cui appare il supereroe più ricorrente.

7. **Matrice di correlazione**  
   Visualizza le correlazioni tra variabili numeriche.

8. **Esci**  
   Termina l'applicazione.

---

## 🧹 Pulizia e Preprocessing

Il modulo `clening.py` si occupa di:
- Conversioni di tipo (`datetime`, `int`, `float`)
- Rimozione caratteri speciali nei dati numerici
- Normalizzazione dei punteggi
- Parsing delle liste di supereroi

---

## 📦 Output

- `risultati_guadagni_mcu.csv`: CSV esportato contenente i dati di profitto analizzati.

---

## 📌 Note

- Il dataset viene caricato da `mcu-movies-updated.csv`, assicurati che sia presente nella directory.
- Il campo `superheroes` viene suddiviso in lista per analisi più granulari.
- Le visualizzazioni sono create con `matplotlib`.

---

## 💡 Idee per Espansioni Future

- Integrazione con API (es. IMDb, TMDB)
- Dashboard interattiva con `Plotly` o `Streamlit`
- Analisi NLP sulle trame
- Classificazione automatica dei film per fase

---

## 🧑‍💻 Autore

Creato con ❤️ da Maresca Ciro, Lilliana Gilca , Stefano Raimondi
Per domande o contributi, apri una *Issue* o una *Pull Request*.
