class Solution:
    def isValid(self, s: str) -> bool:
        lastopen = []
        stdopen = 0
        sqopen = 0
        curlopen = 0

        for i in range(len(s)):
            if s[i] == '(':
                lastopen.append("std")

            if s[i] == '[':
                lastopen.append("sq")

            if s[i] == '{':
                lastopen.append("curl")
            
            if s[i] == ')':
                if lastopen == [] or lastopen[-1] != "std":
                    return False
                lastopen.pop()

            if s[i] == ']':
                if lastopen == [] or lastopen[-1] != "sq":
                    return False
                lastopen.pop()

            if s[i] == '}':
                if lastopen == [] or lastopen[-1] != "curl":
                    return False
                lastopen.pop()

        if lastopen == []:
            return True
        else:
            return False        
                           
               
               

