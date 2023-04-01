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
            self.none.prev = x
        self.none.next = x

    def list_delete(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev

    def list_search(self, k):
        x = self.none.next
        while x is not None and x.key != k and x != self.none:
            x = x.next
        return False if x is self.none else x

    def print_list(self):
        if not self.none.next:
            print("List is empty")
            return
        curr = self.none.next
        while curr != self.none:
            print(curr.key)
            curr = curr.next
        print("End of List")

    def copy_without_repeated_elements(self):
        new_list = LinkedList()
        curr = self.none.prev
        while curr != self.none:
            if not new_list.list_search(curr.key):
                new_list.list_insert(Node(curr.key))
            curr = curr.prev
        return new_list

    def merge_to_new_list(self, list2):
        new_list = LinkedList()
        curr = self.none.prev
        while curr != self.none:
            new_list.list_insert(Node(curr.key))
            curr = curr.prev
        curr = list2.none.prev
        while curr != list2.none:
            new_list.list_insert(Node(curr.key))
            curr = curr.prev
        return new_list


list = LinkedList()
list.list_insert(Node(1))
list.list_insert(Node(2))
list.list_insert(Node(3))
second_list = LinkedList()
second_list.list_insert(Node(4))
second_list.list_insert(Node(5))
second_list.list_insert(Node(6))
list.print_list()
list.copy_without_repeated_elements().print_list()
list.merge_to_new_list(second_list).print_list()
