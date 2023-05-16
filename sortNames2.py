import sys

text_datei = open(sys.argv[len(sys.argv) - 1])
input_list = [line.strip() for line in text_datei]

# Funktion zum vergleich von namen im format "vorname" " " "nachname" lexikographisch
# a <= b == True
def comp(x, y):
    nachnamestartx = 0
    nachnamestarty = 0
    # Bestimme den start der nachnamen von x und y
    for i in range(0, len(x) - 1):
        if x[i] == " ":
            nachnamestartx = i + 1
    for i in range(0, len(y) - 1):
        if y[i] == " ":
            nachnamestarty = i + 1
    
    # Flag für den Fall, dass die nachnamen gleich sind
    nachnamengleich = False 
    
    # Prüfe, wer nach den Nachnamen oben stehen würde
    if x[nachnamestartx:] < y[nachnamestarty:]:
        return True
    elif x[nachnamestartx:] > y[nachnamestarty:]:
        return False
    elif x[nachnamestartx:] == y[nachnamestarty:]:
        nachnamengleich = True # Nachnamen gleich -> prüfe Vornamen
    
    # Prüfe Reihenfolge nach den Vornamen
    if nachnamengleich:
        if x[:nachnamestartx - 2] <= y[:nachnamestarty - 2]:
            return True
        else:
            return False
        

def mergesort(input_list):
    if len(input_list) <= 1: # Basisfall, wenn len(liste) < 2
        return input_list
    mid = len(input_list) // 2
    left = mergesort(input_list[:mid]) # Aufteilung rechts links und sortieren
    right = mergesort(input_list[mid:]) # Aufteilung rechts links und sortieren
    return merge(left, right) #Rückgabe der Liste


def merge(left, right):
    result = []
    i = 0 # Index links
    j = 0 # Index rechts
    while i < len(left) and j < len(right):
        # Pruefe, ob das linke Element kleiner ist
        if comp(left[i], right[j]):
            result.append(left[i]) # linkes Element in Rueckgabeliste einfuegen
            i += 1
        else:
            result.append(right[j]) # rechtes Element in Rueckgabeliste einfuegen
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def partition(input_list, unten, oben):
    pivot = input_list[oben] # rechteste element als pivot
    i = unten - 1 # Teilungsanzeiger
    for j in range(unten, oben):
        if comp(input_list[j], pivot):
            i += 1 # Zeiger um einen anheben
            (input_list[i], input_list[j]) = (input_list[j], input_list[i]) # tausche elemente <= pivot an stelle <= i
    (input_list[i + 1], input_list[oben]) = (input_list[oben], input_list[i + 1]) # tausche pivot an die passende stelle hinter i
    return i + 1


def quicksort(input_list, unten, oben):
    if unten < oben:
        # finde pivot
        p = partition(input_list, unten, oben)
        # rekursiv links
        quicksort(input_list, unten, p - 1)
        # rekursiv rechts
        quicksort(input_list, p + 1, oben)


if sys.argv[1] == '-merge':  # Aufruf wenn -merge als Argument mitgegeben wird
    sorted_list = mergesort(input_list)
    for element in sorted_list:
        print(element)  # Rückgabe an die Konsole (das soll so oder?!)
elif sys.argv[1] == '-quick':  # Aufruf wenn -quick als Argument mitgegeben wird
    quicksort(input_list, 0, len(input_list) - 1) 
    for element in input_list:
        print(element)  # Rückgabe an die Konsole (das soll so oder?!)

text_datei.close()
