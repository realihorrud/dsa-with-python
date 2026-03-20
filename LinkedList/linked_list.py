class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def create_linked_list(self):
        node1 = Node(80)
        self.head = node1

        node2 = Node(32)
        node1.next = node2

        node3 = Node(58)
        node2.next = node3

    def traverse_linked_list(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

    def calculate_sum(self):
        current = self.head
        result = 0
        while current:
            result += current.data
            current = current.next
        return result


linked_list = LinkedList()
linked_list.create_linked_list()
linked_list.traverse_linked_list()
print(linked_list.calculate_sum())
