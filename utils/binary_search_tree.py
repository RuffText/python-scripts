class BinarySearchTree:
    class Node:
        def __init__(self, key) -> None:
            self.left = None
            self.right = None
            self.parent = None
            self.key = key
            self.value = None

        def __repr__(self) -> str:
            return f"({self.key}, {self.value})"

    def __init__(self) -> None:
        self.root = None

    def __contains__(self, key: int) -> bool:
        current_node = self.root
        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return True

        return False

    def __iter__(self):
        yield from self._in_order_traversal(self.root)

    def __repr__(self) -> str:
        return str(list(self._in_order_traversal(self.root)))

    def insert(self, key: int, value: any) -> None:
        if self.root is None:
            self.root = self.Node(key)
            self.root.value = value
        else:
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left is None:
                        current_node.left = self.Node(key)
                        current_node.left.value = value
                        current_node.left.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                elif key > current_node.key:
                    if current_node.right is None:
                        current_node.right = self.Node(key)
                        current_node.right.value = value
                        current_node.right.parent = current_node
                        break
                    else:
                        current_node = current_node.right
                else:
                    current_node.value = value
                    break

    def search(self, key) -> Node | None:
        current_node = self.root
        while True:
            if current_node is None or current_node.key == key:
                return current_node
            elif key < current_node.key:
                if current_node.left is None:
                    return None
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    return None
                else:
                    current_node = current_node.right

    def delete(self, key: int) -> None:
        node = self.search(key)
        if node is None:
            raise KeyError(f"Node with key {key} doesn't exist")

        self._delete(node)

    def traverse(self, order):
        match order.lower():
            case "inorder":
                yield from self._in_order_traversal(self.root)
            case "preorder":
                yield from self._pre_order_traversal(self.root)
            case "postorder":
                yield from self._post_order_traversal(self.root)

    def _delete(self, node: Node) -> None:
        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            else:
                if node.parent.right == node:
                    node.parent.right = None
                else:
                    node.parent.left = None
                node.parent = None

        elif node.left is None or node.right is None:
            child_node = node.left if node.left is not None else node.right

            if node.parent is None:
                child_node.parent = None
                self.root = child_node
            else:
                if node.parent.right == node:
                    node.parent.right = child_node
                else:
                    node.parent.left = child_node
                    child_node.parent = node.parent
        else:
            successor = self._successor(node)

            node.key = successor.key
            node.value = successor.value

            self._delete(successor)

    def _successor(self, node: Node) -> Node | None:
        if node is None:
            raise ValueError("Can't find successor of None")
        if node.right is None:
            return None
        else:
            current_node = node.right
            while current_node.left is not None:
                current_node = current_node.left
            return current_node

    def _predecessor(self, node: Node) -> Node | None:
        if node is None:
            raise ValueError("Can't find predecessor of None")
        if node.left is None:
            return None
        else:
            current_node = node.left
            while current_node.right is not None:
                current_node = current_node.right
            return current_node

    def _in_order_traversal(self, node):
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield (node.key, node.value)
            yield from self._in_order_traversal(node.right)

    def _pre_order_traversal(self, node):
        if node is not None:
            yield (node.key, node.value)
            yield from self._pre_order_traversal(node.left)
            yield from self._pre_order_traversal(node.right)

    def _post_order_traversal(self, node):
        if node is not None:
            yield from self._post_order_traversal(node.left)
            yield from self._post_order_traversal(node.right)
            yield (node.key, node.value)


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(1, "first")
    tree.insert(4, "second")
    tree.insert(2, "third")
    tree.insert(3, "fourth")

    print(tree)

    for i in tree:
        print(i)
