class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        p=[0]*(len(nums)+1)
        for i in range(len(nums)):
            p[i+1]=nums[i]+p[i]
        return p[1:]
