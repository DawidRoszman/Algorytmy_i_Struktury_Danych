class Node:
    def __init__(self, k):
        self.key = k
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listInsert(self, x):
        # wstawia wezel x do listy L
        # lista dwukierunkowa niecykliczna bez wartownika
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def listDelete(self, x):
        # usuwa wezel x z listy
        # lista dwukierunkowa niecykliczna bez wartownika
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev

    def listSearch(self, k):
        # szuka wezla zawierajacego klucz k
        # lista dwukierunkowa cykliczna z wartownikiem
        x = self.none.next
        while x is not None and x.key != k:
            x = x.next
        return x  # wynik “none” oznacza, ze szukanego klucza
        # nie ma na lisciev
