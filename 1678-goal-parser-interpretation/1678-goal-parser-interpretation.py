class Solution:
    def interpret(self, command: str) -> str:
        s=command.replace("()","o")
        s1=""
        for i in s:
            if i != "(" and i!=")":
                s1+=i
        return s1
        