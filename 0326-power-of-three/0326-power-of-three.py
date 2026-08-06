class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        p=1
        while p<=n:
            if p==n:
                return True
            p*=3
        return False