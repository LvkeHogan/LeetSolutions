class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        ptr0 = 0
        ptr1 = len(s) - 1
        listS = list(s)
        
        while(ptr0 < ptr1):
            if listS[ptr0] not in vowels:
                ptr0 += 1
            if listS[ptr1] not in vowels:
                ptr1 -= 1
            if listS[ptr0] in vowels and listS[ptr1] in vowels:
                holder = listS[ptr0]
                listS[ptr0] = listS[ptr1]
                listS[ptr1] = holder
                ptr0 += 1
                ptr1 -= 1
        s = "".join(listS)
        return s
        