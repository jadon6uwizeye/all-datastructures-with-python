class ArrrayStack():

    def __init__(self):
        self._data = []

    def is_empty(self):
        return (len(self.data) == 0)

    def push(self, obj):
        return self._data.append(obj)

    def pop(self):
        if self._data.is_empty():
            return Exception('empty stack')

        return self._data.pop()

    def top(self):
        if self._data.is_empty():
            return Exception('empty stack')

        return self._data[-1]

    def len(self):
        return len(self._data)