from collections import deque


# Node to store the data (Linked List)
class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value


# LRU Cache Data Structure
class LRUCache:

    def __init__(self, max_size):
        self.max_size = max(max_size, 1)
        self.l = deque()
        self.m = {}

    def insert_key_value(self, key, value):
        """
        Time Complexity = O(1)
        """
        # 2 cases
        if key in self.m:
            # replace the old value and update
            it = self.m[key]
            it.value = value
        else:
            # check if cache is full or not
            # remove the least recently used item from cache
            if len(self.l) == self.max_size:
                last = self.l[-1]
                del self.m[last.key]  # remove from hash map
                self.l.pop()  # remove from linked list

            n = Node(key, value)
            self.l.appendleft(n)
            self.m[key] = n

    def get_value(self, key):
        """
        Time Complexity = O(1)
        """
        if key in self.m:
            it = self.m[key]
            value = it.value
            self.l.remove(it)
            self.l.appendleft(it)
            return self.l[0].value
        return None

    def most_recent_key(self):
        """
        Time Complexity = O(1)
        """
        if self.l:
            return self.l[0].key
        return None
