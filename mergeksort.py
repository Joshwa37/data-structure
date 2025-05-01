# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.head=None
    def mergeKLists(self, lists):
        lis=[]
        for i in lists:
            itr=i
            while(itr):
                lis.append(itr.val)
                itr=itr.next
        lis.sort()
        p=None
        per=None
        for i in range(len(lis)-1,-1,-1):
            per=ListNode(lis[i],p)
            p=per
        return per
            
                

        

        
    

        