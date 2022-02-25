from typing import List

class Solution1:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dict = set()
        for num in nums:
            if num in dict:
                return num
            else:
                dict.add(num)
        return -1

class Solution2:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    tmp = nums[nums[i]]
                    nums[nums[i]] = nums[i]
                    nums[i] = tmp
        return -1

