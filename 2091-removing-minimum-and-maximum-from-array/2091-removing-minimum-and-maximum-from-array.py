class Solution(object):
    def minimumDeletions(self, nums):
        n=len(nums)
        x=nums.index(max(nums))
        y=nums.index(min(nums))
        return min(max(x,y)+1,n-min(x,y),min(x,y)+1+n-max(x,y))