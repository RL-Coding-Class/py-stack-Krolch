class Stack:
    """Provides stack container"""
    def __init__(self):
        self._items = []

    def push(self, data):
        self._items.append(data)
        return None

    def pop(self):
        if self._items == None:
            return None
        self._items.pop()

    def get(self):
        if self._items == None:
            return None
        z = self._items[-1]
        return z
    def length(self):
        self._items.count()

    def __str__(self):
        pass

    def __repr__(self):
        pass
