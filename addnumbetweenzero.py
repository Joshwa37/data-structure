# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        itr=head
        count=0
        next=None
        sum=0
        while(itr):
            if(itr.val==0 and count==0):
                count+=1
            elif(itr.val==0 and count==1):
                prev=ListNode(sum,next)
                next=prev
                sum=0
            if(count==1):
                sum+=itr.val     
            itr=itr.next
        itr=prev
        prev1=None
        while(itr):
            next=itr.next
            itr.next=prev1
            prev1=itr
            itr=next
        return prev1