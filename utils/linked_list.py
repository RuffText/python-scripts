class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None

    def __repr__(self):
        if self.head is None:
            return "[]"
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current.value))
            current = current.next
        return "[" + ", ".join(nodes) + "]"

    def __contains__(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __len__(self):
        current = self.head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
        return counter
    
    def append(self, value):
        if self.head is None:
            self.head = self.Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = self.Node(value)

    def prepend(self, value):
        first_node = self.Node(value)
        first_node.next = self.head
        self.head = first_node

    def insert(self, index, value):
        if index < 0:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(value)
            return
        
        if self.head is None:
            raise IndexError("Index out of bounds")
            
        last = self.head
        for i in range(index - 1):
            if last.next is None:
                raise IndexError("Index out of bounds")
            last = last.next

        new_node = self.Node(value)
        new_node.next = last.next
        last.next = new_node

    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
            
        last = self.head
        while last.next:
            if last.next.value == value:
                last.next = last.next.next
                return
            last = last.next

    def pop(self, index):
        if self.head is None or index < 0:
            raise IndexError("Index out of bounds")
            
        if index == 0:
            popped_value = self.head.value
            self.head = self.head.next
            return popped_value

        last = self.head
        for i in range(index - 1):
            if last.next is None:
                raise IndexError("Index out of bounds")
            last = last.next

        if last.next is None:
            raise IndexError("Index out of bounds")
            
        popped_value = last.next.value
        last.next = last.next.next
        return popped_value

    def get(self, index):
        if self.head is None or index < 0:
            raise IndexError("Index out of bounds")
            
        current = self.head
        for i in range(index):
            current = current.next
            if current is None:
                raise IndexError("Index out of bounds")
        return current.value

    def __str__(self):
        if self.head is None:
            return "Empty List"
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.value))
            current = current.next
        nodes.append("None")
        return " -> ".join(nodes)

if __name__ == "__main__":
    pass