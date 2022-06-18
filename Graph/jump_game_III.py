# https://leetcode.com/problems/jump-game-iii/

from typing import List


def dfs(source, arr, visited, ans):
    visited[source] = True

    if arr[source] == 0:
        ans["res"] = True
        return

    forward = source + arr[source]
    if forward < len(arr) and not visited[forward]:
        dfs(forward, arr, visited, ans)

    backward = source - arr[source]
    if backward >= 0 and not visited[backward]:
        dfs(backward, arr, visited, ans)

    visited[source] = False


def can_reach(arr: List[int], start: int) -> bool:
    n = len(arr)
    ans = {"res": False}
    visited = [False] * n
    dfs(start, arr, visited, ans)
    return ans["res"]
