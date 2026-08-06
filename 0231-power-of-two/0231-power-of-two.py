class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        p=1
        while p<=n and p<2**31:
            if p==n:
                return True
            p*=2
        return False