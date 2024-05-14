# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        ptrCount = 1
        evenList = ListNode(0,None)
        evenPtr = evenList
        oddList = ListNode(0,None)
        oddPtr = oddList

        while ptr != None:
            if ptrCount % 2 != 0:
                oddPtr.next = ListNode(ptr.val,None)
                oddPtr = oddPtr.next
                ptr = ptr.next
                ptrCount += 1
            else:
                evenPtr.next = ListNode(ptr.val,None)
                evenPtr = evenPtr.next
                ptr = ptr.next
                ptrCount += 1
        
        #put together even and odd lists

        oddPtr = oddList
        while oddPtr.next != None:
            oddPtr = oddPtr.next
        oddPtr.next = evenList.next
        return oddList.next

