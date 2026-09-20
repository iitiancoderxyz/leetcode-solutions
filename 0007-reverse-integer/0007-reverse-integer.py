class Solution:
    def reverse(self, x: int) -> int:
            if x>=0:
                a=int(str(x)[::-1])
                return a if a<2**31 - 1 else 0
            elif x<0:
                a=int(str(-1*x)[::-1])*-1
                return a if a>-2**31 else 0
            else:
                return 0

            