# https://leetcode.com/problems/word-ladder
from collections import deque
from typing import List


def ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    q = deque([beginWord])
    wordList = set(wordList)
    visited = set()
    visited.add(beginWord)
    step = 0
    while q:
        size = len(q)
        step += 1
        while size:
            curr = q.popleft()
            if curr == endWord:
                return step
            for i, ch in enumerate(curr):
                for char in range(26):
                    char = chr(97 + char)
                    new_string = curr[:i] + char + curr[i + 1:]
                    if new_string in wordList and new_string not in visited:
                        q.append(new_string)
                        visited.add(new_string)

            size -= 1
    return 0
