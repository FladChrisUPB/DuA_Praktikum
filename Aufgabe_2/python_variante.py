import sys

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    input_list = [line.strip() for line in file if not line.startswith(
        "#") and line.strip() != ""]
hash_table = None


def hashCreate(size):
    max_size = 2 ** 16
    table_size = min(size, max_size) # erstellt eine Liste mit leeren Listen
    return [[] for _ in range(table_size)]


def _hash(key, size):
    return hash(key) % size  # hashfunktion für die Liste


def hashSearch(T, key):
    hashindex = _hash(key, len(T))
    for item in T[hashindex]:  # prüft ob es ein item mit dem key gibt
        if item == key:
            return 'true'
    return 'false'


def hashInsert(T, key):
    hashindex = _hash(key, len(T))
    for item in T[hashindex]:
        if item == key:
            return 'false'  # es gibt bereits ein item mit dem key
    T[hashindex].append(key)
    return 'true'  # es gibt kein item mit dem key und es wurde eingefügt


def hashRemove(T, key):
    hashindex = _hash(key, len(T))
    removed = 'false'
    for item in T[hashindex]:
        if item == key:
            T[hashindex].remove(item)
            removed = 'true'
    return removed  # 'true', wenn mindestens ein Element entfernt wurde, sonst 'false'

for line in input_list:
    first_part, last_part = line.split(' ')

    if first_part == 'ins':
        if hash_table is None:
            hash_table = hashCreate(len(last_part))
        result = hashInsert(hash_table, last_part)
        print(f'ins {result}')

    elif first_part == 'del':
        result = hashRemove(hash_table, last_part)
        result = result.lower()
        print(f'del {result}')

    elif first_part == 'search':
        result = hashSearch(hash_table, last_part)
        print(f'search {result}')
