# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:

            return head

        t1 =  head

        t2 = head.next

        while(t2):

            t3 = t2.next

            t2.next = t1

            if t1==head:

                t1.next = None

            
            t1 = t2

            t2 = t3

        return t1
        