class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self,head):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def inset_all_value(self,datas):
        for data in datas:
            self.insert_at_begining(data)
    
    def insert_at_end(self,data):
        if(self.head==None):
            self.insert_at_begining(data)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None)
    
    def get_length(self):
        count=0
        itr=self.head
        while itr.next:
            count+=1
            itr=itr.next
        return count

    def print(self):
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)
            itr=itr.next
        return llstr
    
    

    
