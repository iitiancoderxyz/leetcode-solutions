class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math
        if n<=0:
            return False
        a=round(math.log(n, 3))
        return 3**a== n