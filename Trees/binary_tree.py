from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order(node, res):
    if node is None:
        return

    # Traverse the left subtree first
    in_order(node.left, res)

    # Visit the current node
    res.append(node.data)

    # Traverse the right subtree last
    in_order(node.right, res)


def pre_order(node, res):
    if node is None:
        return

    # Visit the current node first
    res.append(node.data)

    # Traverse the left subtree
    pre_order(node.left, res)

    # Traverse the right subtree
    pre_order(node.right, res)


def post_order(node, res):
    if node is None:
        return

    # First we traverse left subtree
    post_order(node.left, res)

    # After visiting left, traverse right subtree
    post_order(node.right, res)

    # now we visit node
    res.append(node.data)


def level_order_rec(root, level, res):
    # Base case
    if root is None:
        return

    # Add a new level to the result if needed
    if len(res) <= level:
        res.append([])

    # Add current node's data to its corresponding level
    res[level].append(root.data)

    # Recur for left and right children
    level_order_rec(root.left, level + 1, res)
    level_order_rec(root.right, level + 1, res)

# Function to perform level order traversal


def level_order(root):
    # Stores the result level by level
    res = []
    level_order_rec(root, 0, res)
    return res


def height(node):
    if node is None:
        return -1

    l_height = height(node.left)
    r_height = height(node.right)

    result = max(l_height, r_height) + 1

    return result


def get_level(root, target, level):
    if root is None:
        return -1

    if root.data == target:
        return level

    # Recursively call for left and right subtrees
    left_level = get_level(root.left, target, level + 1)
    if left_level != -1:
        return left_level

    return get_level(root.right, target, level + 1)


def if_node_exists(root, target):
    if root is None:
        return False

    if root.data == target:
        return True

    res1 = if_node_exists(root.left, target)
    if res1:
        return True

    res2 = if_node_exists(root.right, target)
    if res2:
        return True


def find_parent(root, target, parent):
    if root is None:
        return -1

    if root.data == target:
        return parent

    left_search = find_parent(root.left, target, root.data)

    if left_search != -1:
        return left_search

    return find_parent(root.right, target, root.data)


def inersert_node(root, data):
    if root is None:
        root = Node(data)
        return root

    q = deque()
    q.append(root)

    while q:
        current = q.popleft()

        if current.left is not None:
            q.append(current.left)
        else:
            current.left = Node(data)
            return root

        if current.right is not None:
            q.append(current.right)
        else:
            current.right = Node(data)
            return root

def delete_deepest_node(root, d_node):
    queue = [root]

    while queue:
        current = queue.pop(0)

        if current == d_node:
            current = None
            del d_node
            return

        if current.right:
            if current.right == d_node:
                current.right = None
                del d_node
                return
            queue.append(current.right)

        if current.left:
            if current.left == d_node:
                current.left = None
                del d_node
                return
            queue.append(current.left)
            
        

def delete_node(root, key):
    if root is None:
        return

    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root
    queue = [root]
    curr = None
    keyNode = None

    # Level order traversal to find the
    # deepest node and the key node
    while queue:
        curr = queue.pop(0)

        # If current node is the key node
        if curr.data == key:
            keyNode = curr

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)

    # If key node is found, replace its
    # data with the deepest node
    if keyNode is not None:
      
        x = curr.data
        
        # Replace key node data with 
        # deepest node's data
        keyNode.data = x
        
        # Delete the deepest node
        delete_deepest_node(root, curr)

    return root
    
def print_leaf_nodes(root):
    if (not root):
        return
    
    if (not root.left and not root.right):
        print(root.data, end = " ")
        return
    
    if root.left:
        print_leaf_nodes(root.left)

    if root.right:
        print_leaf_nodes(root.right)
        

if __name__ == "__main__":
    # Create binary tree
    #      1
    #     / \
    #    2       3
    #   /  \    / \
    #  4    5  50  6
    # /  \    / \
    # 40  50  500 600
    root = Node(1)

    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(40)
    root.left.left.right = Node(50)

    root.right = Node(3)
    root.right.left = Node(50)
    root.right.right = Node(6)
    root.right.left.left = Node(500)
    root.right.left.right = Node(600)

    res = []
    # in_order(root, res)
    # pre_order(root, res)
    post_order(root, res)

    for node in res:
        print(node, end=" ")

    print()

    res = level_order(root)

    for level in res:
        print(' '.join(map(str, level)))

    print("Height of the given Binary Tree is:", height(root))
    print("Level of the given Binary Tree:", get_level(root, 3, 0))
    print("If the given node in Binary Tree exists:", if_node_exists(root, 600))
    print("Parent of 600 is:", find_parent(root, 600, -1))

    key = 1000
    root = inersert_node(root, key)
    print(level_order(root))

    delete_node(root, key)
    print(level_order(root))

    print("Leaf nodes")
    print_leaf_nodes(root)
    print()
