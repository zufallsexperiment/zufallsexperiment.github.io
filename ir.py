import random
import matplotlib.pyplot as plt

# Funktion zum Würfeln
def roll_dice():
    return random.randint(1, 6)

# Funktion, um eine bestimmte Anzahl von Würfen zu simulieren
def simulate_dice_rolls(number_of_rolls):
    results = [roll_dice() for _ in range(number_of_rolls)]
    return results

# Funktion, um die Ergebnisse in einem Histogramm darzustellen
def plot_dice_results(results):
    # Zählen der Vorkommen jeder Augenzahl
    roll_counts = [results.count(i) for i in range(1, 7)]
    
    # Diagramm erstellen
    plt.bar(range(1, 7), roll_counts, tick_label=range(1, 7))
    plt.xlabel("Augenzahl")
    plt.ylabel("Anzahl der Würfe")
    plt.title("Verteilung der Würfelwürfe")
    plt.show()

# Hauptprogramm
if __name__ == "__main__":
    try:
        # Benutzer fragt nach der Anzahl der Würfelwürfe
        number_of_rolls = int(input("Wie viele Würfelwürfe sollen simuliert werden? "))

        # Ergebnisse simulieren
        results = simulate_dice_rolls(number_of_rolls)

        # Ergebnisse plotten
        plot_dice_results(results)
    
    except ValueError:
        print("Bitte geben Sie eine gültige ganze Zahl ein.")

