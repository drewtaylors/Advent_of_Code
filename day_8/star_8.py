from __future__ import print_function
import re

# input.txt
# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
# A----------------------------------
#     B----------- C-----------
#                      D-----
# A, which has 2 child nodes (B, C) and 3 metadata entries (1, 1, 2).
# B, which has 0 child nodes and 3 metadata entries (10, 11, 12).
# C, which has 1 child node (D) and 1 metadata entry (2).
# D, which has 0 child nodes and 1 metadata entry (99).

class Node:
    def __init__(self):
        self.child_nodes = []
        self.metadata_entries = []
        self.num_child_nodes = 0
        self.num_metadata_entries = 0

class Tree:
    def __init__(self, license_file):
        self.index = 0
        self.all_nodes = []
        self.license_file = license_file
        self.root = self.recursive_builder()
        self.total = self.recursive_addition(self.root)

    def recursive_builder(self):
        node = Node()
        self.all_nodes.append(node)
        node.num_child_nodes = license_file[self.index] # A:2 B:0 C:1 D:0
        self.index += 1
        node.num_metadata_entries = license_file[self.index] # A:3 B:3 C:1 D:1
        self.index += 1

        while len(node.child_nodes) < node.num_child_nodes:
            child_node = self.recursive_builder()
            node.child_nodes.append(child_node)
        
        while len(node.metadata_entries) < node.num_metadata_entries:
            node.metadata_entries.append(license_file[self.index]) # B: [10 11 12]
            self.index += 1

        return node

    def recursive_addition(self, node):
        total = 0

        if node.child_nodes:
            for num in node.metadata_entries:
                try:
                    total += self.recursive_addition(node.child_nodes[num-1])
                except IndexError:
                    pass
        else:
            total += sum(node.metadata_entries)

        return total

if __name__ == "__main__":
    print('main')

    license_file = []

    with open('input.txt', 'rb') as f:
        for line in f:
            rule = []
            license_file = [int(x) for x in re.findall(r'\d+', line)]

    # license_file = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

    tree = Tree(license_file)

    a_total = 0

    for node in tree.all_nodes:
        a_total += sum(node.metadata_entries)

    # part a
    print(a_total)

    # value of node B is 10+11+12=33
    # if a node does have child nodes, the metadata entries 
    # become indexes which refer to those child nodes
    # 1 refers to first child, 0 is None

    # part b
    print(tree.total)

