class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        '''
        #My first approach. Works, but readability and flow can use improvement. Unneeded memory usage.
        l1 = list(word1)
        l2 = list(word2)
        merged = []
        maxrun = len(l1) + len(l2)
        
        for i in range(maxrun + 1):
            if i % 2 == 0:
                if len(l1) == 0:
                    merged = merged + l2
                    return "".join(merged)
                merged.append(l1.pop(0))
                
            else:
                if len(l2) == 0:
                    merged = merged + l1
                    return "".join(merged)
                merged.append(l2.pop(0))
                
        return "".join(merged)
        '''
        #Try 2. Roughly the same runtime, without uneeded memory overhead and better simplicity

        i = 0
        merged = []

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
            i += 1
        return "".join(merged)

        