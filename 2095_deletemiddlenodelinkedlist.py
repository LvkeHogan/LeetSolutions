# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #My quite unoptimized solution that works.
        def removeMiddle(currentNode, previousNode, currentPos):
            if currentNode.next == None:
                if currentPos == 1:
                    previousNode.next = None
                if currentPos == 0:
                    return -1
                return currentPos
            else:
                len = removeMiddle(currentNode.next, currentNode,currentPos+1)
            if currentPos == int(ceil(len / 2)) and currentPos != 0:
                previousNode.next = currentNode.next
            return len

        if removeMiddle(head,None,0) == -1:
            return None
        else:
            return head