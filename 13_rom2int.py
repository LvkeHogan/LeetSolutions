class Solution:
    def romanToInt(self, s: str) -> int:
        convdict = {"I":1,"V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        skipflag = False
        if len(s) == 1:
            return convdict[s[0]]
        for i in range(len(s) - 1):
            first = s[i]
            second = s[i + 1]
            if len(s) == 1:
                sum = sum + convdict[second]
            elif skipflag == True:
                skipflag = False
                if i == len(s) - 2:
                    sum = sum + convdict[second]
            elif first == "I" and (second == "V" or second == "X") or first == "X" and (second == "L" or second == "C") or first == "C" and (second == "D" or second == "M"):
                sum = sum + (convdict[second] - convdict[first])
                skipflag = True
            elif i == (len(s)-2):
                sum = sum + convdict[first] + convdict[second]
            else:
                sum = sum + convdict[first]
        return sum
