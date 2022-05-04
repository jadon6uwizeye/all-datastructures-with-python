class LinkedStack:
# ””” LIFO Stack implementation using a singly linked list for storage.”””
#-------------------------- nested Node class --------------------------
    class Node:
    # ”””Lightweight, nonpublic class for storing a singly linked node.”””
        slots = _element , _next
        # streamline memory usage
        # initialize node’s fields
        def init (self, element, next):
        # reference to user’s element
            self. element = element
            # reference to next node
            self. next = next

    #------------------------------- stack methods -------------------------------
    def init (self):
        # ”””Create an empty stack.”””
        # reference to the head node
        self. head = None
        # number of stack elements
        self. size = 0

    def len (self):
        # ”””Return the number of elements in the stack.”””
        return self. size
        
    def is_empty(self):
        # ”””Return True if the stack is empty.”””
        return self. size == 0


    def push(self, e):
        # ”””Add element e to the top of the stack.”””
        # create and link a new node
        self. head = self. Node(e, self. head)
        self. size += 1


    def top(self):
        # ””” Return (but do not remove) the element at the top of the stack.
        # Raise Empty exception if the stack is empty.
        # ”””
        if self.is_empty( ):
            raise Exception("Stack is empty")
            # top of stack is at head of list

        return self._head._element

    def pop(self):
        if self.is_empty( ):
            raise Exception( "Stack is empty" )
        answer = self. head. element
        # bypass the former top node
        self. head = self. head. next
        self._size -= 1
        return answer