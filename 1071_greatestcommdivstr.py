class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        #define some holder variables
        divisor = ""
        l,r = 0,0

        while r < len(str2):
            testStr = str2[l,r + 1]
            if str1.replace(testStr,"") == "" and str2.replace(testStr,"") == "":
                divisor = testStr
                #no need to store length... it's implied any future divisors will be larger.
            r += 1
        return divisor


        '''
    
        '''
        