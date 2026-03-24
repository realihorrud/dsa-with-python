import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


def add_child(parent, child):
    parent.children.append(child)


def print_parents(node, parent):
    if parent is None:
        print(str(node.data) + " -> NULL")
    else:
        print(str(node.data) + " -> " + str(parent.data))

    for child in node.children:
        print_parents(child, node)

# Function to print children of each node
def print_children(node):
    children_str = " ".join(str(child.data) for child in node.children)
    print(str(node.data) + " -> " + children_str)
    for child in node.children:
        print_children(child)

# Function to print leaf nodes
def print_leaf_nodes(node):
    if not node.children:
        sys.stdout.write(str(node.data) + " ")
        return
    for child in node.children:
        print_leaf_nodes(child)

# Function to print degrees of each node 
def print_degrees(node, parent):
    degree = len(node.children)
    if parent is not None:
        degree += 1
    print(str(node.data) + " -> " + str(degree))

    for child in node.children:
        print_degrees(child, node)


if __name__ == "__main__":
    # Creating nodes
    root = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    # Constructing tree
    add_child(root, n2)
    add_child(root, n3)
    add_child(n2, n4)
    add_child(n2, n5)

    print("Parents of each node:")
    print_parents(root, None)

    print("Children of each node:")
    print_children(root)

    print("Leaf nodes: ")
    print_leaf_nodes(root)
    print("\n")  # Newline after leaf nodes

    print("Degrees of nodes:")
    print_degrees(root, None)
