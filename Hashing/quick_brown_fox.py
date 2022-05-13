def min_bars_helper(s: str, idx: int, m: dict):
    if idx >= len(s):
        return 0

    if dp_array[idx] != -1:
        return dp_array[idx]
    ans = float("+inf")
    current_string = ""

    for j in range(idx, len(s)):
        current_string += s[j]
        if current_string in m:
            if j + 1 < len(dp_array) and dp_array[j + 1] != -1:
                remaining_ans = dp_array[j + 1]
            else:
                remaining_ans = min_bars_helper(s, j + 1, m)
            if remaining_ans != -1:
                ans = min(ans, 1 + remaining_ans)
                if j + 1 < len(dp_array):
                    dp_array[j + 1] = ans

    if ans == float("+inf"):
        return -1
    return ans


all_words = [
    "the",
    "fox",
    "thequickbrownfox",
    "jumps",
    "lazy",
    "lazyfox",
    "highbridge",
    "the",
    "over",
    "bridge",
    "high",
    "tall",
    "quick",
    "brown"
]
s = "thequickbrownfoxjumpsoverthehighbridge"

m = {}

for word in all_words:
    m[word] = None

dp_array = [-1] * len(s)
print(min_bars_helper(s, 0, m) - 1)
