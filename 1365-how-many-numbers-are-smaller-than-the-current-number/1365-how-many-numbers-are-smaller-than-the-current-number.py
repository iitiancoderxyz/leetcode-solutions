class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=sorted(nums)
        l=[]
        for item in nums:
            l.append(a.index(item))
        return l