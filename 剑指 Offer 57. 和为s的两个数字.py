from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] + nums[right] < target:
                left += 1
            while right > left and nums[right] + nums[left] > target:
                right -= 1
            if nums[left] + nums[right] == target:
                return list((nums[left],nums[right]))
        return []
