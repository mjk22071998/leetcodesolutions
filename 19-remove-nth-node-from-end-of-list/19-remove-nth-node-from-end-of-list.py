# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        x=1
        stack=[]
        while temp:
            stack.append(temp)
            temp=temp.next
        while x<=n:
            x+=1
            stack.pop()
        if stack:
            element=stack.pop()
            element.next=element.next.next
        else:
            head=head.next
        return head