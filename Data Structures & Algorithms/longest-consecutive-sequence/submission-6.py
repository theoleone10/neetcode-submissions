class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sort = sorted(nums)
        print(sort)

        streak = 1
        maxStreak = 1

        for i in range(1,len(sort)):
            if sort[i] - sort[i-1] == 1:
                streak += 1
                if maxStreak < streak:
                    maxStreak = streak
            elif sort[i] - sort[i-1] != 0:
                streak = 1
        return maxStreak