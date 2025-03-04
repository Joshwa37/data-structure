class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def inset_all_value(self,datas):
        for data in datas:
            self.insert_at_end(data)
    
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
        print(llstr)
    
    def remove_element(self,data):
        itr=self.head
        while(itr.next):
            if(itr.next.data==data):
                itr.next=itr.next.next
                break
            itr=itr.next
    def remove_index(self,index):
        count=0
        itr=self.head
        while(itr):
            if(count==index-1):
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next
    
    def insert_at_index(self,index,data):
        itr=self.head
        count=0
        if(index==0):
            self.insert_at_begining(data)
        else:
            while(itr):
                if(count==index-1):
                    node=Node(data,itr.next)
                    itr.next=node
                    break
                count+=1
                itr=itr.next
    
    def insert_after_value(self,a_value,data):
        itr=self.head
        while(itr):
            if(itr.data==a_value):
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next



if __name__ =='__main__':
    a=LinkedList()
    a.inset_all_value([1,2,3,4,5,6])
    a.insert_after_value(1,8)
    a.print()