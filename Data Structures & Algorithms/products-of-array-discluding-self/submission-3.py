class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        zeros = []
        for i, num in enumerate(nums):
            if num == 0:
                zeros.append(i)
            else:
                totalProduct *= num
        
        res = []

        if len(zeros) > 1:
            for num in nums:
                res.append(0)
        elif len(zeros) == 1:
            for i, num in enumerate(nums):
                if i == zeros[0]:
                    res.append(totalProduct)
                else:
                    res.append(0)
        else:
            for num in nums:
                res.append(int(totalProduct/num))

        return res
