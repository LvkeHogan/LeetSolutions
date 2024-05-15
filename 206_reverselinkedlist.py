#Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Recursive function to reverse the list
        def reverse(currentNode, previousNode):
            #Base case
            if currentNode == None:
                return previousNode
            
            reversedList = reverse(currentNode.next, currentNode)


            #reverse the link
            currentNode.next = previousNode
            
            return reversedList

        return reverse(head,None)
