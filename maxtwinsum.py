# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        count=head
        max=0
        size=0
        while(count):
            size+=1
            count=count.next
        bre=size/2
        count1=0
        itr=head
        pre=None
        while(itr):
            if(count1<bre):
                itr=itr.next
            else:
                next=itr.next
                itr.next=pre
                pre=itr
                print("hi")
                itr=next
            count1+=1
        itr=pre
        itr2=head
        while(itr and itr2):
            sum=itr.val+itr2.val
            if(max<sum):
                max=sum
            itr=itr.next
            itr2=itr2.next
        return max



        
        