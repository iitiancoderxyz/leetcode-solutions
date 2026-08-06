class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        a=max(candies)
        for i in candies:
            if i+extraCandies>=a:
                l.append(True)
            else:
                l.append(False)
        return l