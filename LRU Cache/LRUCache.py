from collections import OrderedDict


class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        Time Complexity = O(1)
        Space Complexity = O(1)
        """
        if key not in self.cache: return None
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        """
        Time Complexity = O(1)
        Space Complexity = O(1)
        """
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)

    def most_recent_key(self):
        """
        Time Complexity = O(N)
        Space Complexity = O(N)
        """
        if self.cache:
            it = next(reversed(self.cache))
            return it
        else:
            return None
