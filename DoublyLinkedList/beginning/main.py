class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        temp_node = Node(value=value)
        self.head = temp_node
        self.tail = temp_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        temp_node = Node(value=value)
        if self.head is None:
            self.head = temp_node
            self.tail = temp_node
        else:
            temp_node.prev = self.tail
            self.tail.next = temp_node
            self.tail = temp_node
        self.length += 1
        return True

    def pop(self):
        if self.length < 1:
            return None
        temp_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return temp_node

    def prepend(self, value):
        temp_node = Node(value=value)
        if self.head:
            temp_node.next = self.head
            self.head.prev = temp_node
            self.head = temp_node
        else:
            self.head = temp_node
            self.tail = temp_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length < 1:
            return None
        temp_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return temp_node

    def get(self, index):
        if index >= self.length or index < 0:
            return None
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node

    def set_value(self, index, value):
        temp_node = self.get(index=index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)

        elif index == self.length:
            return self.append(value)

        temp_node = self.get(index=index - 1)

        if temp_node:
            new_node = Node(value)

            new_node.next = temp_node.next
            new_node.prev = temp_node
            temp_node.next = new_node

            self.length += 1
            return True
        else:
            return False

    def remove(self, index):
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp_node = self.get(index=index)
        if temp_node:
            temp_node.next.prev = temp_node.prev
            temp_node.prev.next = temp_node.next
            return temp_node
        else:
            return None
