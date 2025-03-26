# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        count=0
        add1=None
        addr2=None
        itr=list1
        while(itr):
            if(count==a-1):
                add1=itr
                print(add1.val)
            if(count==b+1):
                addr2=itr
            itr=itr.next
            count+=1
        itr1=list2
        count=0
        while(itr1):
            if(count==0):
                add1.next=itr1
                print(itr1.val)
            if(itr1.next==None):
                itr1.next=addr2
                return list1
            count+=1
            itr1=itr1.next
        


                
        