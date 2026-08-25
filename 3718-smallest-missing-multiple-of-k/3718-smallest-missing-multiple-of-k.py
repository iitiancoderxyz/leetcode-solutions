class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a=max(nums)//k
        s={i*k for i in range(1,a+2)}
        return min(s-set(nums))

        