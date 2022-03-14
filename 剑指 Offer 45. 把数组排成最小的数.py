import functools
from typing import List


class Solution1:
    def minNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(
            lambda x, y: int(x + y) - int(y + x)))
        return "".join(nums)


class Solution2:
    def minNumber(self, nums: List[int]) -> str:
        def quick_sort(l, r):
            if l >= r:
                return
            i, j = l, r
            while i < j:
                while nums[j] + nums[l] >= nums[l] + nums[j] and i < j: j -= 1
                while nums[i] + nums[l] <= nums[l] + nums[i] and i < j: i += 1
                nums[i],nums[j] = nums[j],nums[i]
            nums[i], nums[l] = nums[l], nums[i]
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)

        nums = list(map(str, nums))
        quick_sort(0,len(nums) - 1)
        return ''.join(nums)
