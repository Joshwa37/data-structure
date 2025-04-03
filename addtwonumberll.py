# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        itr=l1
        itr1=l2
        prev=None
        node=None
        num=0
        num1=0
        print(l1.val)
        while(itr):
            next=itr.next
            itr.next=prev
            prev=itr
            itr=next
        while(itr1):
            next=itr1.next
            itr1.next=node
            node=itr1
            itr1=next
        itr=prev
        itr1=node
        while(itr):
            num=num*10+itr.val
            itr=itr.next
        while(itr1):
            num1=num1*10+itr1.val
            itr1=itr1.next
        value=str(num+num1)
        print(num,num1,value)
        node1=None
        prev1=None
        for i in value:
            node1=ListNode(int(i),prev1)
            prev1=node1
        return node1
        