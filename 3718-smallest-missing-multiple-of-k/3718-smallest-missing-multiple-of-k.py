class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        m=max(nums)
        a=m//k
        for i in range(1,a+2):
            if i*k not in nums:
                return i*k

        