class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getsize(self,head):
        itr=head
        count=0
        while(itr):
            count+=1
            itr=itr.next
        return count
    def middleNode(self, head):
        count=self.getsize(head)
        if(count%2==0):
            count=(count/2)+1
        else:
            count=(count+1)//2
        itr=head
        chec=1
        while(itr):
            pri=None
            if(chec==count):
                pri=itr
                break
            chec+=1
            itr=itr.next
        return pri

        
            
        