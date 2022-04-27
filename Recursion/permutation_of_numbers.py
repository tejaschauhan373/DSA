# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def print_permutation(self, array_of_characters: list, index: int, answer: list):

        if index == len(array_of_characters) - 1:
            answer.append(array_of_characters)

        for j in range(index, len(array_of_characters)):
            new_arr = array_of_characters.copy()
            new_arr[index], new_arr[j] = new_arr[j], new_arr[index]
            self.print_permutation(new_arr, index + 1, answer)

    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.print_permutation(nums, 0, answer)
        return answer
