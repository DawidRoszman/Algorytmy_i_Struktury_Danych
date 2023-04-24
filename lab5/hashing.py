# Funkcje haszujące

# Funkcja haszująca wbudowana w Pythonie


def hash_w(k, m):
    return hash(k) % m

# Funkcja haszująca h z pierwszego schematu


def hash_d(k, m):
    value = 0
    a = 111
    for char in k:
        value = value * a + ord(char)
    return value % m

# Funkcja haszująca słaba - tylko według pierwszej litery


def hash_s(k, m):
    return ord(k[0]) % m


# Pomiar ilości pustych list, maksymalnej i
# średniej długości niepustych list w tablicy T
def measure(T):
    empty_lists = 0
    max_length = 0
    sum_length = 0
    nonempty_lists = 0
    for lst in T:
        if not lst:
            empty_lists += 1
        else:
            max_length = max(max_length, len(lst))
            sum_length += len(lst)
            nonempty_lists += 1
    avg_length = sum_length / nonempty_lists if nonempty_lists else 0
    return empty_lists, max_length, avg_length


# Funkcja testująca haszowanie dla danego wariantu
def test_hashing(variant, m, keys):
    T = [[] for _ in range(m)]
    for k in keys:
        i = None
        if variant == 'W':
            i = hash_w(k, m)
        elif variant == 'D':
            i = hash_d(k, m)
        elif variant == 'S':
            i = hash_s(k, m)
        else:
            raise ValueError(f'Unknown variant: {variant}')
        T[i].append(k)

    print(f'Variant {variant}{m}:')
    empty_lists, max_length, avg_length = measure(T)
    print(f'Empty lists: {empty_lists}')
    print(f'Max length: {max_length}')
    print(f'Avg length: {avg_length:.2f}')
    print()


# Wczytanie kluczy z pliku
with open('3700.txt', 'r') as f:
    keys = f.read().splitlines()

# Testowanie dla wszystkich wariantów
for m in [17, 1024, 1031]:
    for variant in ['W', 'D', 'S']:
        test_hashing(variant, m, keys)
