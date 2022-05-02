# https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):
        self.old_days = []
        self.count_dict = {}

    def next_brute(self, price: int) -> int:
        """
        Time Complexity = O(N*N)
        Space Complexity = O(1)
        """
        res = 1
        j = len(self.old_days) - 1

        while j >= 0 and self.old_days[j] <= price:
            j -= 1
            res += 1

        self.old_days.append(price)

        return res

    def next_optimal(self, price: int) -> int:
        """
        Time Complexity = O(N*N)
        Space Complexity = O(N)
        """
        res = 1
        j = len(self.old_days) - 1

        while j >= 0 and self.old_days[j] <= price:
            res += self.count_dict[self.old_days[j]]
            j -= self.count_dict[self.old_days[j]]

        self.old_days.append(price)
        self.count_dict[price] = res
        return res
