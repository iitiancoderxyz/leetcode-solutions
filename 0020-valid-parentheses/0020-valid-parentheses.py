class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in range(len(s)):
            if s[i]  in "({[":
                l.append(s[i])
            else:
                if len(l)!=0:
                    if s[i]==")" and l[-1]=="(":
                        l.pop()
                    elif s[i]=="]" and l[-1]=="[":
                        l.pop()
                    elif s[i]=="}" and l[-1]=="{":
                        l.pop()
                    else:
                        return False

                else:
                    return False
        return len(l) == 0