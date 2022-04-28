class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data: int, position: int):
        if position <= 1:
            self.insert_node(data)
            return
        temp = self.head
        new_node = Node(data)
        for i in range(1, position - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def reverse_k_linked_list(self, head, k):
        if head is None:
            return None

        prev = None
        current = head
        cnt = 1
        temp = None

        while current and cnt <= k:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            cnt += 1

        if temp:
            head.next = self.reverse_k_linked_list(temp, k)
        return prev


def merge_linked_list(node_a: Node, node_b: Node):
    if node_a is None:
        return node_b

    if node_b is None:
        return node_a

    if node_a.data > node_b.data:
        node_c = node_b
        node_c.next = merge_linked_list(node_a, node_b.next)
    else:
        node_c = node_a
        node_c.next = merge_linked_list(node_a.next, node_b)

    return node_c


def get_mid_point(head):
    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    mid = get_mid_point(head)

    a = head
    b = mid.next
    mid.next = None

    a = merge_sort_linked_list(a)
    b = merge_sort_linked_list(b)

    return merge_linked_list(a, b)


def print_linked_list(linked_list):
    temp = linked_list.head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


if __name__ == "__main__":
    linked_list_1 = LinkedList()

    linked_list_1.insert_node(10)
    linked_list_1.insert_node(7)
    linked_list_1.insert_node(2)
    linked_list_1.insert_node(1)
    print_linked_list(linked_list_1)

    linked_list_2 = LinkedList()

    linked_list_2.insert_node(9)
    linked_list_2.insert_node(8)
    linked_list_2.insert_node(6)
    linked_list_2.insert_node(3)
    print_linked_list(linked_list_2)

    final = merge_linked_list(linked_list_1.head, linked_list_2.head)
    merge = LinkedList()
    merge.head = final
    print("final")
    print_linked_list(merge)

    linked_list_1.insert_at_position(4, 3)
    # linked_list.insert_at_position(5, 1)
    # linked_list.insert_at_position(6, 0)
    print_linked_list(linked_list_1)
    # linked_list.head = linked_list.reverse_k_linked_list(linked_list.head, 3)
    linked_list_1.reverse_k_linked_list(linked_list_1.head, 3)
    print_linked_list(linked_list_1)

    linked_list_3 = LinkedList()

    linked_list_3.insert_node(1)
    linked_list_3.insert_node(8)
    linked_list_3.insert_node(6)
    linked_list_3.insert_node(5)
    print_linked_list(linked_list_3)
    linked_list_3.head = merge_sort_linked_list(linked_list_3.head)
    print_linked_list(linked_list_3)
