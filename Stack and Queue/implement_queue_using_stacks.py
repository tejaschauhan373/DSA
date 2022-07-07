# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Time Complexity = O(2N) ~= O(N)
        Space Complexity = O(N)
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def push_optimized(self, x: int) -> None:
        """
        Time Complexity = O(2N) ~= O(N)
        Space Complexity = O(N)
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        """
        Time Complexity = O(1)
        Space Complexity = O(1)
        """
        return self.s1.pop()

    def peek(self) -> int:
        """
        Time Complexity = O(1)
        Space Complexity = O(1)
        """
        return self.s1[-1]

    def empty(self) -> bool:
        """
        Time Complexity = O(1)
        Space Complexity = O(1)
        """
        return len(self.s1) == 0
