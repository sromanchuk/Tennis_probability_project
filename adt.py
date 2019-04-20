class Stack :
    """
    Class that represents the ADT called stack.
    """
    def __init__(self):
        """
        Initialize a new empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Adds a new item to the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return an item from the stack.
        """
        return self.items.pop()

    def is_empty(self):
        """
        Return bool whether the stack is empty.
        """
        return (self.items == [])
