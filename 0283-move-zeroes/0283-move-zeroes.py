class Solution:
    def moveZeroes(self, s: List[int]) -> None:
        l=0
        for r in range(len(s)):
            if s[r]!=0:
                s[l],s[r]=s[r],s[l]
                l+=1