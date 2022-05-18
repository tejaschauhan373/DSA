# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List


def letter_combinations_iterative(digits: str) -> List[str]:
    res = []
    mapper = [
        "0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    ]
    if len(digits) == 0:
        return res
    res.append("")

    for digit in digits:
        tmp = []
        chars = mapper[int(digit)]
        for r in res:
            for char in chars:
                tmp.append(r + char)
        res = tmp
    return res


def letter_combinations_recursive(digits: str) -> List[str]:
    if not digits:
        return []
    m = {"2": "abc",
         "3": "def",
         "4": "ghi",
         "5": "jkl",
         "6": "mno",
         "7": "pqrs",
         "8": "tuv",
         "9": "wxyz"
         }
    ret = []

    def dfs(m, digits, path, ret):
        if not digits:
            ret.append(path)
            return
        for c in m[digits[0]]:
            dfs(m, digits[1:], path + c, ret)

    dfs(m, digits, "", ret)
    return ret


print(letter_combinations_recursive("23"))
