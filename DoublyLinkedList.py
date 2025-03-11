class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class LinkedList:
    def __init__(self): 
        self.head=None
        self.tail=None
        self.size=0
     
    def append(self,data):
        node=Node(data)
        if(self.size==0):
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
        self.size+=1
    
    def preappend(self,data):
        node=Node(data)
        if(self.size==0):
            self.head=node
            self.tail=node
        else:
            self.head.prev=node
            node.next=self.head
            self.head=node
        self.size+=1
    
    def addbefore(self,index,data):
        node=Node(data)
        itr=self.head
        previous=None
        count=0
        while(itr):
            if(count==index):
                if not previous:
                    itr.prev=node
                    node.next=itr
                    self.head=node
                else:
                    previous.next=node
                    itr.prev=node
                    node.next=itr
                    node.prev=previous
            else:
                previous=itr
                itr=itr.next
            count+=1
            self.size+=1

    def delete(self,data):
        itr=self.head
        previous=None
        while(itr):
            if(itr.data==data):
                if not previous:
                    if(itr.next):
                        itr=itr.next
                    itr.prev=None
                    self.head=itr
                else:
                    
                    itr=itr.next
                    itr.prev=previous
                    previous.next=itr
            else:
                previous=itr
                itr=itr.next
    def print(self):
        llstr=""
        itr=self.head
        while(itr):
            llstr+=str(itr.data)+" "
            itr=itr.next
        print(llstr)


li=LinkedList()
li.append(2)
li.append(3)
li.append(4)
li.addbefore(1,8)
li.print()
li.delete(8)
li.print()

        