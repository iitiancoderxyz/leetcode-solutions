class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d={}
        a=sorted(nums)
        for i,x in enumerate(a):
            if x not in d:
                d.update({x:i})
        for i in range(len(nums)):
            a[i]=d[nums[i]]
        return a
