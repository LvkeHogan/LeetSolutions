class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from math import gcd
        
        #The sum of the strings needs to be the same. if not, they aren't made up of the same repeating patterns.
        if str1 + str2 == str2 + str1:
            return ""

        #The grestest common denominator/divisor of the length of the strings will correlate to the longest substring. 
        #Since it passed the previous check, we know that both the strings are made up of repeating patterns. It's just a matter of how many. Strange, but works.
        largestDivLen = gcd(len(str1),len(str2))

        return str1[0:largestDivLen]
        
        
        
        '''
        #Fine solution, just slow.
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
