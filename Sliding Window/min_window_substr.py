# https://leetcode.com/problems/minimum-window-substring/

def find_minimum_window_sub_str(s: str, t: str) -> str:
    """
    Time Complexity = O(N)
    Space Complexity = O(N + M)
    """
    dict_t = {}

    for i in t:
        if i in dict_t:
            dict_t[i] += 1
        else:
            dict_t[i] = 1

    dict_s = {}

    cnt = 0
    min_win_len = float("+inf")
    start = 0
    start_idx = 0

    for i in range(len(s)):

        j = s[i]

        if j in dict_s:
            dict_s[j] += 1
        else:
            dict_s[j] = 1

        if dict_t.get(j) is not None and dict_s[j] <= dict_t[j]:
            cnt += 1

        if cnt == len(t):

            while dict_t.get(s[start], 0) == 0 or dict_t.get(s[start], 0) < dict_s[s[start]]:
                dict_s[s[start]] -= 1
                start += 1

            win_size = i - start + 1

            if win_size < min_win_len:
                min_win_len = win_size
                start_idx = start

    if min_win_len == float("+inf"):
        return ""
    else:
        return s[start_idx: start_idx + min_win_len]


print(find_minimum_window_sub_str("ADOBECODEBANC", "ABC"))
