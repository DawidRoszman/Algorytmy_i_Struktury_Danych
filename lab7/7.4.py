import math

class Node:
    def __init__(self, x):
        self.key = x
        self.left = None  # lewy syn
        self.right = None  # prawy syn
        self.p = None  # ojciec


class BST:
    def __init__(self):
        self.root = None

    def BSTsearchR(self, x, k):
        # szuka rekurencyjnie wezla zawierajacego klucz k w poddrzewie o korzeniu x
        if x == None or x.key == k:
            return x  # None oznacza, ze szukanego klucza nie ma w drzewie
        if k < x.key:
            return self.BSTsearchR(x.left, k)
        else:
            return self.BSTsearchR(x.right, k)

    def BSTinsert(self, z):
        # wstawia wezel z do drzewa
        x = self.root
        y = None  # y jest ojcem x
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.p = y
        # drzewo puste
        if y == None:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

    def BSTDelete(self, z):
        # usuwa węzeł "z" z drzewa wersja "naturalna"
        if z.left is None and z.right is None:  # (1) z liść
            if z == self.root:
                self.root = None
            else:
                if z == z.p.left:  # z jest lewym synem
                    z.p.left = None
                else:
                    z.p.right = None
        elif z.left is not None and z.right is not None:  # (3) dwóch synów
            y = self.BSTMinimum(z.right)
            z.key = y.key  # przepisz zawartość węzła y do z
            self.BSTDelete(y)  # przypadek (1) lub (2)
        else:  # (2) jeden syn
            if z.left is None:  # z.right==None
                z.right.p = z.p
                if z == self.root:
                    self.root = z.left
                else:
                    if z == z.p.left:
                        z.p.left = z.right
                    else:
                        z.p.right = z.right
            else:  # z.left==None
                z.left.p = z.p
                if z == self.root:
                    self.root = z.right
                else:
                    if z == z.p.left:
                        z.p.left = z.left
                    else:
                        z.p.right = z.left

    def BSTMinimum(self, x):
        # zwraca skrajny lewy węzeł w poddrzewie o korzeniu x
        # czyli węzeł o najmniejszym kluczu w tym poddrzewie
        while x.left != None:
            x = x.left
        return x

    def BSTinOrder(self, x):
        # przechodzi i drukuje klucze poddrzewa
        # o korzeniu "x" w kolejnosci
        # "wewnętrznej (in order)"
        if x == None: return
        self.BSTinOrder(x.left)
        print(x.key)
        self.BSTinOrder(x.right)

    def BSTinOrderD(self, x, d):
        # “d” to głębokość na której jest węzeł “x”
        if x == None: return

        self.BSTinOrderD(x.left, d + 1)
        print(f"Depth {d}: {x.key}")
        self.BSTinOrderD(x.right, d + 1)

    def BSTinOrderDTo(self, x, d, to):
        # “d” to głębokość na której jest węzeł “x”
        if x is None or d == to:
            return

        self.BSTinOrderDTo(x.left, d + 1, to)
        print(f"Depth {d}: {x.key}")
        self.BSTinOrderDTo(x.right, d + 1, to)

    def BSTfindDepth(self, x, d=0):
        # “d” to głębokość na której jest węzeł “x”
        if x is None:
            return d - 1

        depth1 = self.BSTfindDepth(x.left, d + 1)
        depth2 = self.BSTfindDepth(x.right, d + 1)
        return max(depth1, depth2)
        # depthMax = depth1 if (depth1 > depth2) else depth2

    def BSTsearch(self, k):
        # szuka wezla zawierajacego klucz k
        x = self.root
        while x != None and x.key != k:
            if k < x.key:
                x = x.left
        else:
            x = x.right
        return x


# print(skins)

# print("=============== Przykładowe drzewo ===============")
# tree = BST()
# node1 = Node("1")
# node2 = Node("2")
# node3 = Node("3")
# node4 = Node("4")
# node5 = Node("5")
# node6 = Node("6")
# node7 = Node("7")
# node8 = Node("8")
# node9 = Node("9")
# nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9]

# # Wstawiamy node'y
# for node in nodes:
#     tree.BSTinsert(node)


# print("========== Szukanie ==========")
# print(tree.BSTsearchR(tree.root, "kota"))
# print(tree.BSTsearchR(tree.root, "kotami"))
#
#
# print("========== Wypisywanie ==========")
# tree.BSTinOrderD(tree.root, 0)
# tree.BSTinOrder(tree.root)
# tree.BSTinOrderDTo(tree.root, 0, 3)
#
# print("========== Wypisywanie ==========")
# print("----- Wypisujemy przed usunięciem -----")
# tree.BSTinOrderD(tree.root, 0)
# print("----- Usuwamy 'jabłoń' i szukamy go w drzewie -----")
# tree.BSTDelete(node6)
# print(tree.BSTsearchR(tree.root, "jabłoń"))
# print("----- Wypisujemy po usunięciu -----")
# tree.BSTinOrderD(tree.root, 0)

# print("========== Głębokość ==========")
# print(tree.BSTfindDepth(tree.root))
# root_tree = BST()
# root_node = Node("root")
# root_tree.BSTinsert(root_node)
# print("--- test dla drzewa z samym korzeniem ---")
# print(tree.BSTfindDepth(root_tree.root))

with open('10k-most-common.txt', 'r', encoding="utf-8") as file:
    content = file.readlines()

passwords = [x.strip() for x in content]

tree_of_passwords = BST()
password_node = []
for p in passwords:
    nodeToAdd = Node(p)
    password_node.append(nodeToAdd)
    tree_of_passwords.BSTinsert(nodeToAdd)

tree_of_passwords.BSTinOrderDTo(tree_of_passwords.root, 0, 3)
depth = tree_of_passwords.BSTfindDepth(tree_of_passwords.root)
print(f"Depth of the tree: {depth}")

print("========== Deleting 80% ==========")
del_counter = math.floor(len(passwords) * 0.8)
# print(del_counter)
for p in password_node:
    if del_counter == 0:
        break
    tree_of_passwords.BSTDelete(p)
    del_counter -= 1

print("--- Tree after deleting 80% ---")
# tree_of_skins.BSTinOrderD(tree_of_skins.root, 0)
tree_of_passwords.BSTinOrderDTo(tree_of_passwords.root, 0, 3)

depth = tree_of_passwords.BSTfindDepth(tree_of_passwords.root)
print(f"Depth of tree after deleting 80%: {depth}")
