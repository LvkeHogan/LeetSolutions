from math import floor
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ispalendrome = True

        arraylist = []
        #function to get the linked list into a standard list
        while(head):
            arraylist.append(head.val)
            head = head.next 
        length = len(arraylist)
 
        l, r = 0, length - 1

        while l <= r:
            if arraylist[l] != arraylist[r]:
                ispalendrome = False
            l += 1
            r -= 1

        return ispalendrome