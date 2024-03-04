# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        slow = head

        fast = head

        while(fast):

            if fast.val == val and slow==fast:

                if slow == head:

                    slow = slow.next

                    fast = slow

                    head = slow

                else:


                    slow =  slow.next
    
                    fast = slow

            elif fast.val == val:

                slow.next = fast.next

                fast = fast.next

            else:

                slow =  fast

                fast  = fast.next

        return head

            



        
        # slow = head

        # fast = head

        # if head == None:

        #     return head

        # while(slow.val==val):

        #     slow =  slow.next

        #     fast = fast.next

        #     head = slow

        #     if slow ==None:

        #         return head

        # fast = fast.next

        # while(fast):

        #     if  fast.val==val:

        #         if fast.next==None:

        #             slow.next = None

        #             return head

        #         slow.next =  fast.next

        #         slow  = slow.next

        #         fast =  slow.next

        #     else:

        #         slow = fast

        #         fast =  fast.next

        # return head

