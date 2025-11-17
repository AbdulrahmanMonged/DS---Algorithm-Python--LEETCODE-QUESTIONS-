class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value=value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    def push(self, value):
        new_node = Node(value=value)
        if self.top:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.top:
            temp_node = self.top
            self.top = temp_node.next
            temp_node.next = None
            self.height -= 1
            return temp_node
        return None
        


test_stack = Stack(4)
# test_stack.print_stack()
test_stack.push(5)
test_stack.push(6)
# test_stack.print_stack()
test_stack.pop()
test_stack.pop()
test_stack.pop()
test_stack.pop()
test_stack.pop()
test_stack.print_stack()
