class ArrrayStack():

    def __init__(self):
        self.data = []

    def is_empty(self):
        return (len(self.data) == 0)

    def push(self, obj):
        return self.data.append(obj)

    def pop(self):
        if self.is_empty():
            return Exception('empty stack')

        return self.data.pop()

    def top(self):
        if self.is_empty():
            return Exception('empty stack')

        return self.data[-1]

    def len(self):
        return len(self.data)