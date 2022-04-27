# https://leetcode.com/problems/predict-the-winner/

def predict_winner_brute(nums: list):
    def solve(i, j, chance):
        """
        Brute Force
        """
        if i > j:
            return 0
        if chance == 0:
            return max(nums[i] + solve(i + 1, j, 1), nums[j] + solve(i, j - 1, 1))
        else:
            return min(solve(i + 1, j, 0), solve(i, j - 1, 0))

    two = sum(nums)
    one = solve(0, len(nums) - 1, 0)
    two -= one
    return one >= two


def predict_winner_optimal(nums: list):
    def winner(nums: list, s: int, e: int, memo: list):
        if s == e:
            return nums[s]
        if memo[s][e] != None:
            return memo[s][e]

        a = nums[s] - winner(nums, s + 1, e, memo)
        b = nums[e] - winner(nums, s, e - 1, memo)
        memo[s][e] = max(a, b)
        return memo[s][e]

    memo = [[None for i in range(len(nums))] for j in range(len(nums))]
    s = winner(nums, 0, len(nums) - 1, memo)
    print(memo)
    return s >= 0


print(predict_winner_optimal([1, 5, 233, 7]))
