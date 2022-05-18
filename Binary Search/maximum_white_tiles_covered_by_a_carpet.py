# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet

from typing import List
from bisect import *


def maximum_white_tiles(tiles: List[List[int]], carpet_len: int) -> int:
    # sort the tiles by the starting position
    tiles.sort(key=lambda x: x[0])
    # build the starting position array
    start_pos = [tiles[i][0] for i in range(len(tiles))]
    # build the prefix sum array
    pre_sum = [0] * (len(tiles) + 1)
    for i in range(1, len(tiles) + 1):
        pre_sum[i] = pre_sum[i - 1] + (tiles[i - 1][1] - tiles[i - 1][0] + 1)

    res = 0
    for i in range(len(tiles)):
        s, e = tiles[i]
        # if the length of tile >= length of carpet, return carpetLen
        if e >= s + carpet_len - 1:
            return carpet_len
        # binary search the index of the ending tile that the carpet can partially cover
        end_idx = bisect_right(start_pos, s + carpet_len - 1) - 1
        # calculate the length of the ending tile that the carpet cannot cover
        compensate = 0
        if tiles[end_idx][1] > s + carpet_len - 1:
            compensate = tiles[end_idx][1] - s - carpet_len + 1
        # update the result
        res = max(res, pre_sum[end_idx + 1] - pre_sum[i] - compensate)

    return res


tiles = [[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]]
carpetLen = 10

print(maximum_white_tiles(tiles, carpetLen))
