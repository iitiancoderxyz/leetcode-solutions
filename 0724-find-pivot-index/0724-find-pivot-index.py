class Solution:
    def pivotIndex(self, l: list[int]) -> int:
        a=sum(l)
        s=0
        for i in range(len(l)):
            if s==a-s-l[i]:
                return i
            s+=l[i]
        return -1