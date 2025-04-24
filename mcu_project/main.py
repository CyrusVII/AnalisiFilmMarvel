# main.py
from clening import take_data
from plots import plot_roi, plot_box_office_trend
from analysis import analizza_guadagni_mcu

import matplotlib.pyplot as plt


def menu():
    df = take_data()

    while True:
        print("\n=== MENU MCU ANALYSIS ===")
        print("1. Visualizza ROI per film")
        print("2. Visualizza andamento incassi nel tempo")
        print("3. Analizza guadagni (media, max, min)")
        print("4. Esci")

        scelta = input("Scegli un'opzione (1-4): ")
        match scelta:
            case "1":
                plot_roi(df)
            case "2":
                plot_box_office_trend(df)
            case "3":
                risultati = analizza_guadagni_mcu(df)
                print("\nRisultati guadagni MCU:")
                for k, v in risultati.items():
                    print(f"{k.capitalize()}: {v}")
            case "4":
                print("Uscita dal programma. 👋")
                break
            case _:
                print("Opzione non valida. Riprova.")

# Avvio del menu
if __name__ == "__main__":
    menu()