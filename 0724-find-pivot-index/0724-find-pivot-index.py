class Solution:
    def pivotIndex(self, l: list[int]) -> int:
        for i in range(len(l)):
            if sum(l[:i])==sum(l[i+1:]) and i<len(l):
                return i
        else:
            return -1