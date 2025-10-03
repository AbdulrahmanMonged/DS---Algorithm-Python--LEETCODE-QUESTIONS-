class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        if self.length <= 1:
            return
        dummy_node = Node(None)
        dummy_node.next = self.head
        previous_node = dummy_node
        for _ in range(start_index):
            previous_node = previous_node.next

        current_node = previous_node.next

        for i in range(end_index - start_index):
            temp_node = current_node.next
            current_node.next = temp_node.next
            temp_node.next = previous_node.next
            previous_node.next = temp_node
        self.head = dummy_node.next


ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original linked list: ")
ll.print_list()

# Reverse a sublist within the linked list
ll.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
ll.print_list()

# Reverse another sublist within the linked list
ll.reverse_between(0, 4)
print("Reversed entire linked list: ")
ll.print_list()

# Reverse a sublist of length 1 within the linked list
ll.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
ll.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1 -> 2 -> 3 -> 4 -> 5 -> None
    Reversed sublist (2, 4): 
    1 -> 2 -> 5 -> 4 -> 3 -> None
    Reversed entire linked list: 
    3 -> 4 -> 5 -> 2 -> 1 -> None
    Reversed sublist of length 1 (3, 3): 
    3 -> 4 -> 5 -> 2 -> 1 -> None
    Reversed empty linked list: 
    Empty -> None
    
"""
