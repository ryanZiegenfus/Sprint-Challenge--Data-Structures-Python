import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:                       - This is O(n^2)
#             duplicates.append(name_1)

class BinarySearchTree:
    def __init__(self, value = None, file = None):
        self.value = value
        self.left = None
        self.right = None
        self.file = file

    def insert(self, name, src):
        def rec_f(node = self):
            global duplicates
            if self.value == None:
                self.value = name
            elif node.value == name and node.file != src:
                duplicates += [name]
                return
            elif name > node.value:
                if node.right:
                    rec_f(node.right)
                else:                 
                    node.right = BinarySearchTree(name, src)
            else:
                if node.left:
                    rec_f(node.left)
                else:
                    node.left = BinarySearchTree(name, src)
        rec_f()

x = BinarySearchTree()
for i in names_1:
    x.insert(i, 'names_1')
for j in names_2:
    x.insert(j, 'names_2')

# stretch
# duplicates = set(names_1) & set(names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
