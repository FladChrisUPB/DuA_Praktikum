import argparse
# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def extract_list(pfad):
    #List jede Zeile einer Datei ein und gibt diese als Listenelemente in einer Liste zurück
    #Zeilen die mit # starten gelten als kommentare und werden nicht eingelesen
    namensliste = []
    with open(pfad) as namelist:
        names = namelist.readlines()
        for name in names:
            if name[0] != "#" and name != " ":
                i = 0     # zähler um das leerzeichen zu finden
                for zeichen in name:
                    if zeichen == " ":
                        vorname = name[:i]
                        j = i

                    if zeichen == "\n":
                        nachname = name[j:i]
                        namensliste.append([nachname, vorname])
                        break
                    i += 1

    return namensliste


def mergesort(input_list):
    #mergesort auf liste angewand (ohne möglichkeit eigener/normaler weights)
    if len(input_list) == 0 or len(input_list) == 1:  # wenn 0 oder 1 direkte Rückgabe (Basisfall)
        return input_list
    mid = len(input_list)//2
    left = mergesort(input_list[:mid])
    right = mergesort(input_list[mid:])
    return merge(left, right)   # rückgabe der Liste an das System


def merge(left, right):
    result = []  # passt schon
    i = 0  # linker index
    j = 0  # rechter index
    while i < len(left) and j < len(right):
        # Prüfen ob das linke Element kleiner (Vorrangiger ist)
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        elif left[i][0] != right[j][0]:     # Prüfen ob das rechte Element größer ist
            result.append(right[j])
            j += 1
        # Prüfen ob bei gleichem Nachnamen der Vorname kleiner ist
        elif left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])     # Rest anhängen linker Teilbaum
    result.extend(right[j:])    # Rest anhängen rechter Teilbaum
    return result


def quicksort(namelist):
    #quicksort auf liste angewand (ohne möglichkeit eigener/normaler weights)
    if len(namelist) <= 1:  # Basisfall
        return namelist
    akt_index = namelist[0]     # pivot festlegen
    left = []
    right = []
    for name in namelist[1:]:
        if name[0] < akt_index[0]:
            left.append(name)   # hinzufügen, wenn das Element kleiner ist
        elif name[0] != akt_index[0]:
            right.append(name)  # hinzufügen, wenn das Element größer ist
        elif name[1] < akt_index[1]:
            # hinzufügen, wenn Nachnamen gleich und Element kleiner
            left.append(name)
        else:
            # hinzufügen, wenn Nachnamen gleich und Element größer
            right.append(name)
    # rekursiver aufruf
    return quicksort(left) + [akt_index] + quicksort(right)


def restore_namelist(namelist):
    restored_namelist = []
    for name in namelist:
        restored_namelist.append(name[1] + "" + name[0])
    return restored_namelist


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Sort a txt File (with first and lastnames) with Mergesort and Quicksort")
    parser.add_argument('-quick', dest='quick', action='store_const', const=True,
                        default=False)  # ob quicksortv
    parser.add_argument('-debug', dest='debug', action='store_const', const=True,
                        default=False)  # ob alle sorts
    parser.add_argument('-merge', dest='merge', action='store_const', const=True,
                        default=False)  # ob mergesort
    parser.add_argument('path', type=str)  # pfad der einzulesenden datei
    args = parser.parse_args()  # momentan nur 1 argument drin?

    path = args.path
    soll_quick = args.quick
    soll_merge = args.merge
    soll_debug = args.debug
    namensliste = extract_list(path)

    if soll_quick:
        sorted_list = quicksort(namensliste)
    elif soll_merge:
        sorted_list = mergesort(namensliste)
    elif soll_debug:
        sorted_list = quicksort(namensliste)
        sorted_merge_list = mergesort(namensliste)
        if (sorted_list == sorted_merge_list):
            print("True")
        else:
            print("False")
    else:
        print("use quick- or mergesort pls")

    result = restore_namelist(sorted_list)
    for name in result:
        print(name)
