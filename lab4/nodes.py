class Node:
    def __init__(self, k):
        self.key = k
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.none = Node(None)

    def list_insert(self, x):
        x.prev = self.none
        if self.none.next is not None:
            self.none.next.prev = x
            x.next = self.none.next
        else:
            x.next = self.none
        self.none.next = x

    def list_delete(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev

    def list_search(self, k):
        x = self.none.next
        while x is not None and x.key != k and x != self.none:
            x = x.next
        return "No element in list" if x is self.none else x

    def print_list(self):
        if not self.none.next:
            print("List is empty")
            return
        curr = self.none.next
        while curr != self.none:
            print(curr.key, curr.prev.key, curr.next.key)
            curr = curr.next
        print("End of List")


node = Node(5)
list = LinkedList()
list.list_insert(Node(1))
list.list_insert(Node(2))
list.list_insert(Node(3))
list.list_insert(Node(4))
list.list_insert(node)
list.print_list()
