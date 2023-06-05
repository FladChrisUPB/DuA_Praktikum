import subprocess
import re

# Anzahl der Durchläufe
num_runs = 1000

# Liste für die Sekundenwerte
script1_seconds = []
script2_seconds = []

# Muster für die Extraktion der Sekunden
pattern = r'Gesamtlaufzeit: (\d+(?:\.\d+)?) Sekunden'

for _ in range(num_runs):
    # Erstes Skript aufrufen
    result1 = subprocess.run(
        ['python3', 'python_variante.py', 'a00512.txt'], capture_output=True, text=True)  # Name Skript 1 hier anpassen
    output1 = result1.stdout

    # Sekunden extrahieren
    match1 = re.search(pattern, output1)
    if match1:
        seconds1 = float(match1.group(1))
        script1_seconds.append(seconds1)

    # Zweites Skript aufrufen
    result2 = subprocess.run(
        ['python3', 'textcode_1_fladungc_Aufgabe2.py', 'a00512.txt'], capture_output=True, text=True)  # Name Skript 2 hier anpassen
    output2 = result2.stdout

    # Sekunden extrahieren
    match2 = re.search(pattern, output2)
    if match2:
        seconds2 = float(match2.group(1))
        script2_seconds.append(seconds2)
    

def exclude_zero(values):  # Verhindert, dass 0.0 als minimaler Wert ausgegeben wird
    non_zero_values = [value for value in values if value != 0.0]
    if non_zero_values:
        return min(non_zero_values)
    else:
        return None

# Minimalen, maximalen und durchschnittlichen Wert ausgeben
if script1_seconds:
    min_seconds1 = exclude_zero(script1_seconds)
    max_seconds1 = max(script1_seconds)
    avg_seconds1 = sum(script1_seconds) / len(script1_seconds)
    print("Ergebnisse für Skript 1:")
    print("Minimaler Wert:", min_seconds1)
    print("Maximaler Wert:", max_seconds1)
    print("Durchschnittlicher Wert:", avg_seconds1)
else:
    print("Keine Sekundenwerte gefunden für Skript 1")

if script2_seconds:
    min_seconds2 = exclude_zero(script2_seconds)
    max_seconds2 = max(script2_seconds)
    avg_seconds2 = sum(script2_seconds) / len(script2_seconds)
    print("Ergebnisse für Skript 2:")
    print("Minimaler Wert:", min_seconds2)
    print("Maximaler Wert:", max_seconds2)
    print("Durchschnittlicher Wert:", avg_seconds2)
else:
    print("Keine Sekundenwerte gefunden für Skript 2")

print(num_runs, "Durchläufe")