class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums=set(nums)
        a,b=min(nums),max(nums)
        c=[]
        for i in range(a,b):
            if i not in nums:
                c.append(i)
        return c
                
