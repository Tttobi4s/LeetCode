from re import L
from typing import List


class Solution1:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue
            ma = max(ma,num)
            mi = min(mi,num)
            if num in repeat: return False
            repeat.add(num)
        return ma - mi < 5


class Solution2:
    def isStraight(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort()
        for i in range(4):
            if nums[i] == 0: joker += 1
            elif nums[i] == nums[i + 1]: return False
        return nums[4] - nums[joker] < 5
