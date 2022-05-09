"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.


"""

class MinStack:

    def __init__(self):
        self._data = []
        self._min = None
        
    def push(self, val: int) -> None:
        self._data.append(val)
        if self.getMin() and self.getMin()>val:
            self._min=val

    def pop(self) -> None:
        if self.getMin() == self._data[-1]:
            self._data.pop()
            if(self._data):
                self._min = min(self._data)
            else:
                self._min=None
        else:
            self._data.pop()
            
    def top(self) -> int:
        return self._data[-1]

    def getMin(self) -> int:
        if (len(self._data)==0):
            return None
        
        elif len(self._data) == 1:
            self._min = self._data[-1]
            return(self._min)
        
        elif(not self._min == None):
            return self._min
        
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()