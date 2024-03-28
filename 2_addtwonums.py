# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        sum = 0
        carry = False
        while l1 and l2:
            sum = l1.val + l2.val
            if carry == True:
                sum += 1
                carry = False
            if sum >= 10:
                carry = True
                sum -= 10
            tail.next = ListNode(val = sum)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            if carry == True:
                sum = l1.val + 1
                carry = False
            else:
                sum = l1.val
            if sum >= 10:
                carry = True
                sum = sum - 10
            tail.next = ListNode(val = sum)
            l1 = l1.next
            tail = tail.next

        while l2:
            if carry == True:
                sum = l2.val + 1
                carry = False
            else:
                sum = l2.val
            if sum >= 10:
                carry = True
                sum = sum - 10
            l2 = l2.next
            tail.next = ListNode(val = sum)
            tail = tail.next
        
        if l1 == None and l2 == None and carry == True:
            tail.next = ListNode(val = 1)
            tail = tail.next


        return dummy.next