# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/
def roman_to_int(s: str) -> int:
    i = len(s) - 1
    res = 0
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    while i >= 0:
        temp_res = roman[s[i]]
        while i - 1 >= 0 and roman[s[i - 1]] < roman[s[i]]:
            temp_res -= roman[s[i - 1]]
            i -= 1
        i -= 1
        res += temp_res
    return res
