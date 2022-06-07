# https://leetcode.com/problems/edit-distance/

# Recursive
def min_distance_brute(word1: str, word2: str) -> int:
    """
    Time Complexity = O(2^N)
    Space Complexity = 1 + O(N)
    ; N = len(word1)
    """

    def min_operation(word1: str, word2: str, i: int, j: int):
        # base case
        if i >= len(word1) and j >= len(word2):
            # word1 and word2 over at same point
            # means word1 == word2, no need of any operation
            return 0

        if i >= len(word1):
            # word1 is over, word2 is remaining
            # return no. of characters need to insert in word1
            return len(word2) - j

        if j >= len(word2):
            # word2 is over, word1 is remaining
            # return no. of characters to delete from word1
            return len(word1) - i

        # recursive case
        if word1[i] == word2[j]:
            return min_operation(word1, word2, i + 1, j + 1)

        replace = 1 + min_operation(word1, word2, i + 1, j + 1)
        delete = 1 + min_operation(word1, word2, i + 1, j)
        insert = 1 + min_operation(word1, word2, i, j + 1)
        return min(replace, delete, insert)

    return min_operation(word1, word2, 0, 0)


# Top Down
def min_distance_top_down(word1: str, word2: str):
    """
    Time Complexity = O(N*M)
    Space Complexity = O(N*M)
    ; N = len(word1), M = len(word2)
    """
    l1 = len(word1)
    l2 = len(word2)
    dp = [[-1 for _ in range(l2)] for _ in range(l1)]

    def min_operation(word1: str, word2: str, i: int, j: int, dp: list):

        # base case
        if i >= len(word1) and j >= len(word2):
            # word1 and word2 over at same point
            # means word1 == word2, no need of any operation
            return 0

        if i >= len(word1):
            # word1 is over, word2 is remaining
            # return no. of characters need to insert in word1
            return len(word2) - j

        if j >= len(word2):
            # word2 is over, word1 is remaining
            # return no. of characters to delete from word1
            return len(word1) - i

        # Check if this step is already computed
        if dp[i][j] != -1:
            return dp[i][j]

        # recursive case
        if word1[i] == word2[j]:
            return min_operation(word1, word2, i + 1, j + 1, dp)

        replace = min_operation(word1, word2, i + 1, j + 1, dp)
        delete = min_operation(word1, word2, i + 1, j, dp)
        insert = min_operation(word1, word2, i, j + 1, dp)
        res = 1 + min(replace, delete, insert)  # added cost of 1 to perform any operation
        dp[i][j] = res
        return dp[i][j]

    return min_operation(word1, word2, 0, 0, dp)


# Bottom Up
def min_distance_bottom_up(word1: str, word2: str):
    """
    Time Complexity = O(N*M)
    Space Complexity = O(N*M)
    ; N = len(word1), M = len(word2)
    """
    l1 = len(word1)
    l2 = len(word2)
    dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

    # Base condition
    for i in range(l1 + 1):
        dp[i][0] = i

    for j in range(l2 + 1):
        dp[0][j] = j

    """
    Let's say word1 = "horse", word2 = "ros"
    l1 = len(word1) = 5
    l2 = len(word2) = 3
        
         word2 "" r  o  s 
    word1      
    ""         0  1  2  3     ->  word1 = "" , operation to only insert char. of word2
    h          1  1  2  3
    o          2  2  1  2
    r          3  2  2  2
    s          4  3  3  2
    e          5  4  4  3
    
    """
    # Solving sub problems
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                insert = dp[i][j - 1]
                delete = dp[i - 1][j]
                replace = dp[i - 1][j - 1]

                dp[i][j] = 1 + min(insert, delete, replace)

    # Print Bottom Up DP array
    # for row in dp:
    #     for i in row:
    #         print("%3s" % i, end="")
    #     print()
    return dp[l1][l2]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    print(min_distance_brute(word1, word2))
    print(min_distance_top_down(word1, word2))
    print(min_distance_bottom_up(word1, word2))
