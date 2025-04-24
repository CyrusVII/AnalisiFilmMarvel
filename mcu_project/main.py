# main.py
from clening import take_data
from plots import plot_roi, plot_box_office_trend, visualizza_matrice_correlazione
from analysis import (
    analizza_guadagni_mcu,
    analizza_scores,
    conta_supereroi,
    film_supereroe_piu_presente
)
import matplotlib.pyplot as plt


def menu():
    df = take_data()

    while True:
        print("\n=== MENU MCU ANALYSIS ===")
        print("1. Visualizza ROI per film")
        print("2. Visualizza andamento inc1assi nel tempo")
        print("3. Analizza guadagni (media, max, min)")
        print("4. Analizza critici vs pubblico")
        print("5. Conta supereroi per numero di film")
        print("6. Film in cui appare il supereroe più presente")
        print("7. Film matrice di correlazione")
        print("8. Esci")

        scelta = input("Scegli un'opzione (1-8): ")
        match scelta:
            case "1":
                plot_roi(df)
            case "2":
                plot_box_office_trend(df)
            case "3":
                risultati = analizza_guadagni_mcu(df)
                print("\n📊 Risultati guadagni MCU:")
                for k, v in risultati.items():
                    print(f"{k.capitalize()}: {v}")
            case "4":
                risultati = analizza_scores(df)
                print("\n🍿 Analisi punteggi pubblico vs critici:")
                for chiave, valore in risultati.items():
                    print(f"\n{chiave.upper()}:")
                    for k, v in valore.items():
                        print(f"  {k}: {v}")
            case "5":
                print("\n🦸‍♂️ Conteggio supereroi:")
                conteggio = conta_supereroi(df)
                print(conteggio)
            case "6":
                print("\n🎬 Supereroe più presente e relativi film:")
                film_supereroe_piu_presente(df)
            case "7":
                visualizza_matrice_correlazione(df)
            case "8":
                print("Uscita dal programma. 👋")
                break
            case _:
                print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    menu()
