class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head

        i = 0
        while temp and i < index:
            temp = temp.next
            i += 1

        if temp is None:
            return -1

        return temp.data

    def add_at_head(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def add_at_tail(self, val: int) -> None:

        if self.head is None:
            self.add_at_head(val)
            return

        temp = self.head
        new_node = Node(val)
        while temp and temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def add_at_index(self, index: int, val: int) -> None:
        if index == 0:
            self.add_at_head(val)
            return

        new_node = Node(val)
        temp = self.head

        i = 0

        while temp and i < index - 1:
            temp = temp.next
            i += 1

        if temp is None:
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete_at_index(self, index: int) -> None:

        if index == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return

        if self.head is None:
            return
        temp = self.head
        for i in range(index - 1):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return
        delete_node = temp.next
        if temp.next is None:
            temp.next = None
            return
        temp.next = temp.next.next
        delete_node.next = None


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(0)
obj.add_at_head(1)
obj.add_at_tail(2)
obj.add_at_index(1, 3)
obj.delete_at_index(1)
