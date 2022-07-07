# https://leetcode.com/problems/implement-stack-using-queues
from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Time Complexity = O(2N) ~= O(N)
        Space Complexity = O(N)
        """
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self) -> int:
        """
        Time Complexity = O(1)
        Space Complexity = O(1)
        """
        return self.q1.popleft()

    def top(self) -> int:
        """
        Time Complexity = O(1)
        Space Complexity = O(1)
        """
        return self.q1[0]

    def empty(self) -> bool:
        """
        Time Complexity = O(1)
        Space Complexity = O(1)
        """
        return len(self.q1) == 0
