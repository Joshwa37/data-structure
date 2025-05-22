# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        def size(head):
            itr=head
            count=0
            while(itr):
                count+=1
                itr=itr.next
            return count
        size2=size(head)
        size=size(head)//k
        print(size)
        def connect(pre,head):
            while(head):
                if(head.next==None):
                    head.next=pre
                    break
                head=head.next
            return 0
        itr=head
        pre=None
        rem=None
        light=None
        count=0
        while(itr):
            if(size>0):
                count+=1
                next=itr.next
                itr.next=pre
                pre=itr
                itr=next
                if(count%k==1):
                    light=pre
                    print(pre.val)
                if(count==k):
                    size-=1
                    rem=pre
                    pre=None
                if(count%k==0 and count>k):
                    size-=1
                    connect(pre,rem)
                    pre=None
            else:
                break 
        if(size2%k!=0):
            light.next=itr
        return rem

