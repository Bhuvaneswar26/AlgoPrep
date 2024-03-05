# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head==None:

            return head


        temp = head

        len=1

        while(temp.next):

            len+=1

            temp = temp.next

        print(len)

        temp.next = head

        k = len-(k%len)

        c = 0

        prev =  head

        curr = head

        while(c!=k):

            prev= curr

            curr = curr.next

            c+=1

        prev.next = None

        return curr

            

        

        

