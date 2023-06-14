import random 

# funkcja zwracająca długość najdłuższego wspólnego podciągu
def lcsLength(x, y):
    m = len(x)
    n = len(y)
    # utworzenie tablic c i b
    c = [[0 for i in range(n + 1)]  
         for j in range(m + 1)]  
    b = [[0 for i in range(n + 1)]
         for j in range(m + 1)]
    # wypełnienie tablic zerami

    # wypełnienie tablic c i b
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # jeśli znaki są takie same
                c[i][j] = c[i - 1][j - 1] + 1  # zwiększamy wartość w tablicy c
                b[i][j] = '\\'  # zapisujemy znak w tablicy b
            else:
                if c[i - 1][j] >= c[i][j - 1]:  # jeśli wartość w górnym sąsiedzie jest większa lub równa niż w lewym sąsiedzie
                    c[i][j] = c[i - 1][j]  # przepisujemy wartość z górnego sąsiedniego pola
                    b[i][j] = "|"  # zapisujemy znak w tablicy b
                else:
                    c[i][j] = c[i][j - 1]  # przepisujemy wartość z lewego sąsiedniego pola
                    b[i][j] = "-"  # zapisujemy znak w tablicy b
    return c, b

# funkcja zwracająca najdłuższy wspólny podciąg
def PrintLCS(x, b, i, j):
    if i == 0 or j == 0:
        return []
    if b[i][j] == "\\":  # jeśli znaki są takie same
        lcs = PrintLCS(x, b, i - 1, j - 1)  # rekurencyjnie wywołujemy funkcję dla poprzedniego pola
        lcs.append(x[i - 1])  # dodajemy znak do listy
        return lcs
    elif b[i][j] == "|":  # jeśli wartość w górnym sąsiedzie jest większa lub równa niż w lewym sąsiedzie
        return PrintLCS(x, b, i - 1, j)  # rekurencyjnie wywołujemy funkcję dla górnego pola
    else:
        return PrintLCS(x, b, i, j - 1)  # rekurencyjnie wywołujemy funkcję dla lewego pola

# funkcja zwracająca długość najdłuższego wspólnego podciągu bez użycia pamięci
def lcs_length_without_memory(x, y):
    m = len(x)
    n = len(y)

    prev_row = [0] * (n + 1)
    curr_row = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                curr_row[j] = prev_row[j - 1] + 1
            else:
                curr_row[j] = max(prev_row[j], curr_row[j - 1])

        prev_row = curr_row[:]
        curr_row = [0] * (n + 1)

    return prev_row[n]

# funkcja generująca losowy ciąg znaków
def generate_random_sequence(n, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sequence = [random.choice(alphabet[:k]) for _ in range(n)]
    print(''.join(sequence)+"\n\n")
    return ''.join(sequence)

# lista słów do testowania
list_of_words = ["abcbdab", "bdcaba"]

# wywołanie funkcji lcsLength i PrintLCS
l1, l2 = lcsLength(*list_of_words)
lcs = PrintLCS(list_of_words[0], l2, len(list_of_words[0]), len(list_of_words[1]))
print(f"Najdłuższy wspólny podciąg:", "".join(lcs))

# wywołanie funkcji lcs_length_without_memory
length1 = lcs_length_without_memory(*list_of_words)
print(f"Długość najdłuższego wspólnego podciągu: {length1}")

# testy
print("testy:")
ns = [100, 500, 1000]
ks = [2, 4, 8, 16]

for n in ns:
    for k in ks:
        generated_word_1 = generate_random_sequence(n, k)
        generated_word_2 = generate_random_sequence(n, k)
        length = lcs_length_without_memory(generated_word_1, generated_word_2)
        print(f"Dla n: {n}, dla k: {k}:")
        print(f"Długość najdłuższego wspólnego podciągu: {length}. Iloraz: {length / n}")
        print(f"-------------------------")