class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while n<=100:
            a=str(n)
            prod=1
            for i in a:
                prod*=(int(i))
            if prod%t==0:
                return n
            n+=1

        