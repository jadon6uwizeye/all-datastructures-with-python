class Stack:

    def __init__(self):
        self._data = []

    def push(self, s):
        self._data.append(s)

    def pop(self):
        return self._data.pop()

    def is_empty(self):
        if(len(self._data)):
            return False
        else:
            return True

def match_delimiters(input):

    s = Stack()
    lefty = "({["
    righty = ")}]"

    for i in input:
        if i in lefty:
            s.push(i)
        elif i in righty:
            if (s.is_empty()):
                return False
            if (righty.index(i) != lefty.index(s.pop())):
                return False

        else:
            return Error("unknown symbol")

    return s.is_empty()

print(match_delimiters("[{}{{([])}}]"))