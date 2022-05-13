# https://leetcode.com/problems/find-common-characters/

def common_chars(words):
    """
    Time Complexity = O(len(words)*len(longest_word))
    Space Complexity = O(len(common_characters))
    """

    res_d = {}
    for char in words[0]:
        if char in res_d:
            res_d[char] += 1
        else:
            res_d[char] = 1

    for word in words[1:]:
        new_res = {}
        current_temp = {}
        for char in word:
            if char in current_temp:
                current_temp[char] += 1
            else:
                current_temp[char] = 1

            if char in res_d:
                new_res[char] = min(res_d[char], current_temp[char])
        res_d = new_res

    res = []

    for char, count in res_d.items():
        for i in range(count):
            res.append(char)

    return res
