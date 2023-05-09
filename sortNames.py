import sys

text_datei = open(sys.argv[len(sys.argv)-1])
input_list = str(text_datei.readline())

def mergesort(input_list):
    if len(input_list) == 0 or len(input_list) == 1:  # Wenn 1 oder 0 direkte rückgabe (Basisfall)
        return input_list
    mid = len(input_list) // 2
    left = mergesort(input_list[:mid])
    right = mergesort(input_list[mid:])
    return(merge(left, right))  # Rückgabe der Liste an das system


def merge(left, right):
    result = []  # hier bin ich unsicher, ist das richtig, dass man es als Liste zurück gibt? Ist ja sehr ähnlich einem Array?!
    i = 0  # linker Index
    j = 0  # rechter Index
    while i < len(left) and j < len(right):
        # Prüfen ob das linke Element kleiner (Vorangiger ist)
        if left[i] <= right[j]:
            result.append(left[i])  # linkes Element wird hinzugefügt
            i += 1
        else:
            result.append(right[j])  # rechtes Element wird hinzugefügt
            j += 1
    result.extend(left[i:])  # Rest anhängen linke Teilbaum
    result.extend(right[j:])  # Rest anhängen rechter Teilbaum
    return result


def quicksort(input_list):
    if len(input_list) <= 1:  # Basisfall
        return input_list
    akt_index = input_list[0]  # Pivot festlegen
    left = []
    right = []
    for input_list in input_list[1:]:
        if input_list < akt_index:
            left.append(input_list)  # hinzufügen wenn das Element kleiner ist
        else:
            right.append(input_list)  # hinzufügen wen ndas Element größer ist
    return(quicksort(left) + [akt_index] + quicksort(right))  # rekursiver aufruf


if sys.argv[1] == '-merge':
    sorted_list = mergesort(input_list)
    for element in sorted_list:
        print(element)
elif sys.argv[1] == '-quick':
    sorted_list = quicksort(input_list)
    for element in sorted_list:
        print(element)

text_datei.close()
