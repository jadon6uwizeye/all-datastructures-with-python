
class  Node:
    def  __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return value

        self.tail.next = Node(value)
        self.tail = self.tail.next
        return value

    def pop(self):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.next is None:
            value = self.head.data
            self.head = None
            self.tail = None
            return value

        node = self.head
        while node.next.next is not None:
            node = node.next

        value = node.next.data
        node.next = None
        self.tail = node
        return value

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def __repr__(self):
        return f"LinkedList({', '.join(str(value) for value in self)})"


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.pop()
    ll.append(3)
    ll.append(4)
    print(ll)
    print("\n\n")
    for value in ll.__iter__():
        print(value)
