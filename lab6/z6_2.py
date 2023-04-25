import random
# S + OK

def hash_d(k):
    value = 0
    a = 111
    for char in k:
        value = value * a + ord(char)
    return value


# def hash_d(k, m):
#     value = 1
#     a = 111
#     for i in range(1, len(k)):
#         value = value * (a+ ord(k[i - 1]) + ord(k[i]))
#     return value % m

# def hash_d(k):
#     return hash(k)

class Obj:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def __str__(self):
        return f"{self.name} {self.number}"


with open("./nazwiskaASCII.txt") as file:
    names = file.readlines()
    names = [name.strip().split(" ") for name in names]
    names = [Obj(int(name[0]), name[1]) for name in names]

with open("./pierwsze.txt") as file:
    lines = [x.split(" ") for x in file.readlines()]
    stripped = []
    for line in lines:
        for num in line:
            if num != '':
                stripped.append(int(num.strip()))

first100 = names[:100]


def h(k, i): return (hash_d(k) + 25*i + 25*(i**2))


# Open hashing with cubic probing
table_size = 151
hash_table = [None] * table_size


def hash_insert(key, hash_table):
    i = 0
    while i < len(hash_table):
        j = (h(key.name, i) % len(hash_table)) 
        if hash_table[j] is None:
            hash_table[j] = key.name
            return j
        i += 1
    print("Hash table is full")
    return


def hash_search(key, hash_table):
    i = 0
    while i < len(hash_table):
        j = (h(key.name, i) % len(hash_table))
        if hash_table[j] is None:
            print("Liczba prób:", i)
            return None
        if hash_table[j] == key:
            print("Liczba prób:", i)
            return j
        i += 1
    print("Liczba prób:", i)
    return None

for name in first100:
    hash_insert(name, hash_table)

for i in range(20):
    print(hash_search(first100[i], hash_table))

print(hash_table)


# print(hash_table)


# test for bigger table couple of thousands
size_of_table2 = 25733
hash_table2 = [None] * size_of_table2

for name in names:
    hash_insert(name, hash_table2)

# search last 20 names
for i in range(20):
    print(hash_search(names[-i], hash_table2))
