# https://leetcode.com/problems/longest-palindromic-subsequence/

def longestPalindromeSubseq(s: str) -> int:
    """
    Time Complexity = O(N^2)
    Space Complexity = O(N)
    """

    def find_palindrome(i, j, deleted, res):
        if i >= 0 and j < n:
            if s[i] == s[j]:
                find_palindrome(i - 1, j + 1, deleted, res)
            else:
                find_palindrome(i, j + 1, deleted + 1, res)
                find_palindrome(i - 1, j, deleted + 1, res)
        else:
            res["ans"] = max(res["ans"], (((j - 1) - (i + 1)) + 1) - deleted)

    res = {"ans": 0}
    n = len(s)
    for index in range(n):
        find_palindrome(index, index, 0, res)
        find_palindrome(index, index + 1, 0, res)
    return res["ans"]


string = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
print(longestPalindromeSubseq(string))
