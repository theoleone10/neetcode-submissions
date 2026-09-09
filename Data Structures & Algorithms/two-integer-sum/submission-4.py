class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}

        for i, num in enumerate(nums):
            if num in hash:
                return [hash[num],i]

            hash[target - num] = i
