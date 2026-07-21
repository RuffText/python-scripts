class DoublyLinkedList:

    class Node:

        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None

    def __init__(self):
        self.head = None
        self.tail = None

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
        new_node = self.Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def prepend(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

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
        new_node.previous = last

        if last.next is not None:
            last.next.previous = new_node
        else:
            self.tail = new_node

        last.next = new_node

    def delete(self, value):
        if self.head is None:
            return

        current = self.head
        while current is not None:
            if current.value == value:
                if current.previous is not None:
                    current.previous.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                return
            current = current.next

    def pop(self, index):
        if self.head is None or index < 0:
            raise IndexError("Index out of bounds")

        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next

        if current is None:
            raise IndexError("Index out of bounds")

        popped_value = current.value

        if current.previous is not None:
            current.previous.next = current.next
        else:
            self.head = current.next

        if current.next is not None:
            current.next.previous = current.previous
        else:
            self.tail = current.previous

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