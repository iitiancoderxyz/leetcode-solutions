class Solution:
    def reverseDegree(self, st: str) -> int:
        a="abcdefghijklmnopqrstuvwxyz"
        s=0
        for i in range(len(st)):
            x=26-a.index(st[i])
            s+=(x)*(i+1)
        return s