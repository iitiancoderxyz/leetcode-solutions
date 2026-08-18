class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in range (len(nums)):
            if nums[i] not in d:
                d.update({nums[i]:1})
            else:
                d[nums[i]]+=1
        for j in d:
            if d[j]==1:
                return j
                break
