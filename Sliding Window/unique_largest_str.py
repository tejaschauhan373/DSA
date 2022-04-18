# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def length_of_longest_substring(s: str) -> int:
    """
    Time Complexity = O(N)
    Space Complexity = O(N)
    """
    if len(s) == 0:
        return 0

    i = 0
    j = 0
    window_len = 0
    max_l = 0
    start_win = -1

    m = {}

    while j < len(s):
        ele = s[j]

        if ele in m and m[ele] >= i:
            i = m[ele] + 1
            window_len = j - i

        m[ele] = j
        window_len += 1
        j += 1

        if window_len > max_l:
            max_l = window_len
            start_win = i

    print("Largest unique string => ", s[start_win: start_win + max_l])
    return max_l


print(length_of_longest_substring("abbabcabcd"))
