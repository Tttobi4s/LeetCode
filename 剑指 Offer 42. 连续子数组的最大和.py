from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, pre = nums[0], nums[0]
        for i in range(1, len(nums)):
            if pre < 0:
                cur = nums[i]
            else:
                cur = pre + nums[i]
            res = max(res, cur)
            pre = cur
        return res